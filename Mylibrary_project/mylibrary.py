# LIBRARY MANAGMENT SISTEM
# SIMPLE SISTEM TO MANAGE LOAN FROM A LIBRARY
# FUNCIONATIES: 1 - REGISTER USERS AND BOOKS (FUNCTIONS READY)
#               2 - REGISTER AND MANAGMENT OF LOANS (FUNCTIONS READY)
#               3 - REPORTS (MOST POPULAR BOOKS, USER WITH MOST LOANS,...)
#               4 - INTERFACE

# DB mylibrary: TABLES: users: user_id(SERIAL), first_name, last_name, email(NOT NULL UNIQUE), created_on, last_login
#                       books: book_id(SERIAL), title, author, copies_available, created_at
#                       loans: loan_id(SERIAL), user_id(F.KEY), book_id(F.KEY), loan_date, return_date

import csv, datetime 
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
def add_data_from_file():

    while True:
        try:
            print("Input 1 for users` data.\nInput 2 for books` data.\nInput 0 to cancel")
            choice = int(input("\nType here: "))
            if choice not in [0,1,2]:
                print("Invalid input. (0, 1 or 2)")
                continue
            elif choice == 0:
                return print("Input of data was cancelled.")
            else:
                while True:
                    file_path = input("Please input the .csv file path: Type 0 to return.\n")
                    file_path = file_path.strip('"')
                    if file_path == '0':
                        break
                    if not file_path.endswith('.csv'):
                        print("Not an .csv file")
                        continue
                    else:
                        break  
                if file_path == '0':
                    continue
                else:
                    break
        except:
            print("Invalid input. (0, 1 or 2)")
    try:
        data = open(file_path,encoding = 'utf-8')
        csv_data = csv.reader(data)
        data_lines = list(csv_data)
    except FileNotFoundError:
        return print("That`s not a valid .csv path file")
    
    if choice == 1:
        total_users = total_users()
        for index, header in enumerate(data_lines[0]):
            if header.lower() == 'name':
                name_index = index
            elif header.lower() == 'email':
                email_index = index

        for row in data_lines[1:]:
            name = row[name_index]
            name_parts = name.split()
            first_name = name_parts[0]
            last_name = name_parts[-1]
            email = row[email_index]
            add_user(first_name,last_name,email)

        cursor.execute("SELECT COUNT(*) FROM users")
        new_total_users = cursor.fetchone()[0]
        new_users = new_total_users - total_users
        return print(f"{new_users} new users added to Database.")
    
    if choice == 2:
        total_books = total_books()
        for index, header in enumerate(data_lines[0]):
            if header.lower() == 'title':
                title_index = index
            elif header.lower() == 'author':
                author_index = index
            elif header.lower() == 'copies_available':
                copies_index = index

        for row in data_lines[1:]:
            title = row[title_index]
            author = row[author_index]
            copies = row[copies_index]
            add_book(title,author,copies)

        new_total_books = total_books()
        new_books = new_total_books - total_books

        return print(f"{new_books} new books added to Database.")

def add_user(first_name,last_name,email):
    first_name = first_name.title()
    last_name = last_name.title()
    try:
        cursor.execute("INSERT INTO users(first_name,last_name,email,last_login) VALUES(%s,%s,%s,%s) RETURNING user_id", (first_name,last_name,email,datetime.datetime.now()))
        conn.commit()
        return print(f" User added successfully. user_id = {cursor.fetchone()[0]}")
    except pg2.errors.UniqueViolation:
        conn.rollback()
        return print(f"Error: The email: {email} is already in use.")

def add_book(title,author,copies = 1):
    cursor.execute("SELECT COUNT(book_id) FROM books WHERE title ILIKE %s", ('%' + title + '%',))
    book_in_database = cursor.fetchone()[0]
    if book_in_database:
        cursor.execute("UPDATE books SET copies_available = copies_available + %s WHERE title ILIKE %s RETURNING book_id",(copies,title))
        conn.commit()
        return print(f"Added {copies} copies of the book: {title} Id: {cursor.fetchone()[0]}")
    
    else:
        title = title.title()
        author = author.title()
        cursor.execute("INSERT INTO books(title,author,copies_available) VALUES(%s,%s,%s) RETURNING book_id", (title,author,copies))
        conn.commit()
        return print(f" Book added successfully. book_id = {cursor.fetchone()[0]}")

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
    return print(f"Book returned successfully")

def loan_emulator(loan_quantity):
    cursor.execute("SELECT user_id FROM users")
    all_users_id = cursor.fetchall() # LIST of tuples (user_id,)
    cursor.execute("SELECT book_id FROM books")
    all_books_id = cursor.fetchall() # LIST of tuples (book_id,)

    for loan in range(loan_quantity):
        user_id = rd.choice(all_users_id)[0]
        book_id = rd.choice(all_books_id)[0]

        loan_book(user_id,book_id)

def book_popularity_report(book_quantity=10): #UNFINISHED 
    cursor.execute("""SELECT books.book_id, title, COUNT(*) AS total_loans FROM loans
                        JOIN books ON books.book_id = loans.book_id
                        GROUP BY books.book_id, title
                        ORDER BY total_loans DESC
                        LIMIT %s""",(book_quantity,))

    report = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]
    report_visualisation = pd.DataFrame(report, columns=columns)

    print(report_visualisation)

book_popularity_report()