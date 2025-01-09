# LIBRARY MANAGMENT SISTEM
# SIMPLE SISTEM TO MANAGE LOAN FROM A LIBRARY
# FUNCIONATIES: 1 - REGISTER USERS AND BOOKS (FUNCTIONS READY)
#               2 - REGISTER AND MANAGMENT OF LOANS (FUNCTIONS READY)
#               3 - REPORTS (MOST POPULAR BOOKS, USER WITH MOST LOANS,...)
#               4 - INTERFACE

# DB mylibrary: TABLES: users: user_id(SERIAL), first_name, last_name, email(NOT NULL UNIQUE), created_on, last_login
#                       books: book_id(SERIAL), title, author, copies_available, created_at
#                       loans: loan_id(SERIAL), user_id(F.KEY), book_id(F.KEY), loan_date, return_date

import os, datetime 
import psycopg2 as pg2
import random as rd
import pandas as pd

# Connection with Postgres Database
conn = pg2.connect(dbname="mylibrary_project", user="postgres", password="373500")
cursor = conn.cursor()

# Return total users from the database
def total_users():
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]

def total_books():
    cursor.execute("SELECT COUNT(*) FROM books")
    return cursor.fetchone()[0]
#Function to add data from a .csv file to the Database
def add_data():

    data = file_reader()
    table_name = input("Input here the table`s name that you wish to add this data to: ")
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
    except pg2.errors.UndefinedTable:
        conn.rollback()
        return print("There isn't a table with this name.")
    while True:
        cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")
        db_users_headers = cursor.fetchall() # LIST of tuples (header,)
        db_users_headers = [header[0] for header in db_users_headers] # MADE A DIRECT LIST OF HEADERS
        new_headers = [column for column in (set(data.columns) - set(db_users_headers))]

        if new_headers != []:
            print(f"These are the columns not present on our DataBase: " + ', '.join(new_headers))
            choice = input("Would you like to include a new column into our database? Y or N").lower().strip()[0]
            if choice not in ['y','n']:
                print("Invalid option: Try Y or N.")
                continue

            if choice == 'y':
                while True:
                    print("From the following, choose what column to input in our Database. Type in the respective number (one at a time): ")
                    for index, header in enumerate(new_headers):
                        print(index, ' - ' + header)
                    try:
                        index_new_header = int(input().strip())
                        column_name = new_headers[index_new_header]
                    except ValueError or IndexError:
                        print("Not a valid option.")
                        continue
                    data_type_options = ('INT','VARCHAR','DATE','TIMESTAMP')
                    while True:
                        print(f"Must choose a data type for the column {column_name}. Type in the respective number: ")
                        for index, data_type in enumerate(data_type_options):
                            print(index, ' - ' + data_type)
                        try:
                            index_data_type = int(input().strip())
                            column_data_type = data_type_options[index_data_type]
                            query = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_data_type}"
                            cursor.execute(query)
                            conn.commit()
                        except ValueError or IndexError:
                            print("Not a valid option.")
                            continue
                        break

                    break
            else:
                break
        else:
            break

    for row in data.iterrows():
        row_data = row[1]
        columns_names = set(db_users_headers) & set(data.columns)
        if table_name == 'users':
            add_user(row_data,columns_names)
        if table_name == 'books':
            add_book(row_data,columns_names)

    return print(f"Database updated.")
    
    if "book_id" in data.columns:
        cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'books'")
        db_books_headers = cursor.fetchall() # LIST of tuples (header,)
        
        total_books = total_books()
        for index, header in enumerate(data[0]):
            if header.lower() == 'title':
                title_index = index
            elif header.lower() == 'author':
                author_index = index
            elif header.lower() == 'copies_available':
                copies_index = index

        for row in data:
            title = row[title_index]
            author = row[author_index]
            copies = row[copies_index]
            add_book(title,author,copies)

        new_total_books = total_books()
        new_books = new_total_books - total_books

        return print(f"{new_books} new books added to Database.")

def add_user(user_data,columns_names): # recebe listas(data_user,db_headers)
    try:
        columns_names_to_insert = ', '.join(columns_names)
        values = ''
        excluded_query = ''
        for column in columns_names:
            if values == '':
                values += "'" + str(user_data[column]) + "'"
            else:
                values += ", '" + str(user_data[column]) + "'"

            if excluded_query == '':
                excluded_query += column + ' = EXCLUDED.' + column
            else:
                excluded_query += ", " + column + ' = EXCLUDED.' + column
        query = f"""
        INSERT INTO users({columns_names_to_insert}) VALUES({values})
        ON CONFLICT (email)
        DO UPDATE SET {excluded_query}
        RETURNING user_id
        """
        cursor.execute(query)
        conn.commit()
        return print(f" User added/updated successfully. user_id = {cursor.fetchone()[0]}")
    except pg2.errors.UniqueViolation:
        conn.rollback()
        return print(f"Error: The email: {user_data['email']} is already in use.")

def add_book(book_data,columns_names):
    try:
        columns_names_to_insert = ', '.join(columns_names)
        values = ''
        excluded_query = ''
        for column in columns_names:
            if values == '':
                values += "'" + str(book_data[column]) + "'"
            else:
                values += ", '" + str(book_data[column]) + "'"

            if column == 'copies_available':
                new_copies_available = book_data[column]
                continue

            if excluded_query == '':
                excluded_query += column + ' = EXCLUDED.' + column
            else:
                excluded_query += ", " + column + ' = EXCLUDED.' + column
        query = f"""
        INSERT INTO books({columns_names_to_insert}) VALUES({values})
        ON CONFLICT (author, title)
        DO UPDATE SET {excluded_query}, copies_available = EXCLUDED.copies_available + {new_copies_available}
        RETURNING book_id
        """
        cursor.execute(query)
        conn.commit()
        return print(f" Book added/updated successfully. book_id = {cursor.fetchone()[0]}")
    except pg2.errors.UniqueViolation:
        conn.rollback()
        return print(f"Error: The book: {book_data['title']} from Author: {book_data['author']} is already in DataBase")

def loan_book(user_id,book_id):

    cursor.execute("SELECT copies_available FROM books WHERE book_id = %s", (book_id,))
    copies_available = cursor.fetchone()[0]
    if copies_available == 0:
        return print(f"The book has no copies avaiable at this moment")
    else:
        cursor.execute("INSERT INTO loans(user_id,book_id,loan_date) VALUES(%s,%s,%s) RETURNING loan_id",(user_id,book_id, datetime.datetime.now()))
        loan_id = cursor.fetchone()[0]
        cursor.execute("UPDATE books SET copies_available = copies_available - 1 WHERE book_id = %s",(book_id,))
        cursor.execute("UPDATE users SET last_login = %s WHERE user_id = %s" , (datetime.datetime.now(),user_id))
        conn.commit()
        return print(f"Loan successfully made. ID: {loan_id}")
    
def return_book(loan_id):
    cursor.execute("SELECT user_id,book_id FROM loans WHERE loan_id = %s", (loan_id,))
    loan_data = cursor.fetchone()
    user_id = loan_data[0]
    book_id = loan_data[1]
    cursor.execute("UPDATE users SET last_login = %s WHERE user_id = %s" , (datetime.datetime.now(),user_id))
    cursor.execute("UPDATE books SET copies_available = copies_available + 1 WHERE book_id = %s" , (book_id,))
    cursor.execute("UPDATE loans SET return_date = %s WHERE loan_id = %s" , (datetime.datetime.now(),loan_id))
    conn.commit()
    return print(f"Loan {loan_id} finished. Book returned successfully")

def loan_simulator(loan_quantity): #Simulates random loans
    cursor.execute("SELECT user_id FROM users")
    all_users_id = cursor.fetchall() # LIST of tuples (user_id,)
    cursor.execute("SELECT book_id FROM books WHERE copies_available > 0")
    all_books_id = cursor.fetchall() # LIST of tuples (book_id,)

    for loan in range(loan_quantity):
        user_id = rd.choice(all_users_id)[0]
        book_id = rd.choice(all_books_id)[0]

        loan_book(user_id,book_id)
        cursor.execute("SELECT copies_available FROM books WHERE book_id = %s",(book_id,))
        if cursor.fetchone()[0] == 0:
            all_books_id.remove((book_id,))

def return_simulator(return_quantity): # Simulates random returns

    cursor.execute("SELECT loan_id FROM loans WHERE return_date IS NULL")
    open_loans_id = cursor.fetchall()  # LIST of tuples (loan_id,)
    if open_loans_id != []:
        if return_quantity > len(open_loans_id):
            return_quantity = len(open_loans_id)

        for loan in range(return_quantity):
            index_loan = rd.randrange(len(open_loans_id))
            chosen_loan = open_loans_id.pop(index_loan)
            loan_id = chosen_loan[0]
            return_book(loan_id)
    
    else:
        return print("There are no open loans at this moment.")

def book_popularity_report(book_quantity=None): # If no parameter is passed, return the whole report
    cursor.execute("""SELECT books.book_id, title, COUNT(*) AS total_loans FROM loans
                        JOIN books ON books.book_id = loans.book_id
                        GROUP BY books.book_id, title
                        ORDER BY total_loans DESC
                        LIMIT %s""",(book_quantity,))

    report = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]
    report_visualisation = pd.DataFrame(report, columns=columns)

    print(report_visualisation.to_string(index=False))

def users_activity_report(user_quantity=None):
    cursor.execute("""SELECT users.user_id, first_name, last_name, COUNT(*) AS total_loans FROM loans
                    JOIN users ON users.user_id = loans.user_id
                    GROUP BY users.user_id, first_name, last_name
                    ORDER BY total_loans DESC
                    LIMIT %s""",(user_quantity,))

    report = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]
    report_visualisation = pd.DataFrame(report, columns=columns)

    print(report_visualisation.to_string(index=False))

def reports_menu():
    valid_options = ["0","1","2"]
    while True:
        print("""
Welcome to the report`s menu. Right now we`ve only a few options of reports, but feel free to try.
    1 - Books Popularity.
    2 - Users Activity.
    0 - Quit
""")

        choice = input("Type here: ").strip()

        if choice not in valid_options:
            print("Invalid option.")
            continue

        if choice == "0":
            print("Quitting the report`s menu. Bye")
            break

        if choice == "1":
            book_popularity_report()
            break

        if choice == "2":
            users_activity_report()
            break

def file_reader(): 
    supported_file_ext = ['.csv','.json','.xml','.xls', '.xlsx']
    while True:    
        file_path = input("Input path file here: ").strip('"')

        if not os.path.isfile(file_path):
            print("File not found. Please check the path and try again.")
            continue

        file_ext = os.path.splitext(file_path)[1]
        if file_ext not in supported_file_ext:
            print(f"Unsupported file extension. Supported extensions: {', '.join(supported_file_ext)}")
            continue
    
        try:
            if file_ext == ".csv":
                data = pd.read_csv(file_path,encoding = 'utf-8')
            if file_ext == ".json":
                data = pd.read_json(file_path,encoding = 'utf-8')
            if file_ext == ".xml":
                data = pd.read_xml(file_path,encoding = 'utf-8')
            if file_ext in [".xls", ".xlsx"]:
                data = pd.read_excel(file_path,encoding = 'utf-8')

            print("File loaded successfully!")
            return data
        
        except Exception as e:
            print(f"An error occurred while loading the file: {e}")
            return None

add_data()