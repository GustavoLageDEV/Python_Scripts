# LIBRARY MANAGMENT SISTEM
# SIMPLE SISTEM TO MANAGE LOAN FROM A LIBRARY
# FUNCIONATIES: 1 - REGISTER USERS AND BOOKS (FUNCTIONS READY)
#               2 - REGISTER AND MANAGMENT OF LOANS (FUNCTIONS READY)
#               3 - REPORTS (MOST POPULAR BOOKS, USER WITH MOST LOANS,...)
#               4 - INTERFACE

# DB mylibrary: TABLES: users: user_id(SERIAL), first_name, last_name, email(NOT NULL UNIQUE), created_on, last_login
#                       books: book_id, title, author, copies_avaiable, created_at
#                       loans: loan_id, user_id, book_id, loan_date, return_date

import csv
import psycopg2 as pg2
import datetime 

# Conexão com o banco de dados
conn = pg2.connect(dbname="mylibrary_project", user="postgres", password="373500")

cursor = conn.cursor()

def add_data():
    while True:
        try:
            choice = int(input("Input 1 for users` data.\nInput 2 for books` data.\nInput 0 to cancel"))
            if choice not in [0,1,2]:
                print("Invalid input. (0, 1 or 2)")
                continue
            elif choice == 0:
                return print("Input of data was cancelled.")
            else:
                while True:
                    data_file = input("Please input the .csv file path:")
                    if not data_file.endswith('.csv'):
                        print("Not an .csv file")
                        continue
                    else:
                        break

                break     
        except:
            print("Invalid input. (0, 1 or 2)")

    data = open(data_file,encoding = 'utf-8')
    csv_data = csv.reader(data)
    data_lines = list(csv_data)
    
    if choice == 1:
        for index, header in enumerate(data_lines[0]):
            if header == 'name':
                name_index = index
            elif header == 'email':
                email_index = index

        for 

def add_user(first_name,last_name,email):
    
    cursor.execute("INSERT INTO users(first_name,last_name,email,last_login) VALUES(%s,%s,%s,%s) RETURNING user_id", (first_name,last_name,email,datetime.datetime.now()))
    conn.commit()
    return print(f" User added successfully. user_id = {cursor.fetchone()[0]}")

def add_book(title,author,copies = 1):
    
    cursor.execute("INSERT INTO books(title,author,copies_avaiable) VALUES(%s,%s,%s) RETURNING book_id", (title,author,copies))
    conn.commit()
    return print(f" Book added successfully. book_id = {cursor.fetchone()[0]}")

def loan_book(user_id,book_id):

    cursor.execute("SELECT copies_avaiable FROM books WHERE book_id = %s", (book_id,))
    copies_avaiable = cursor.fetchone()[0]
    if copies_avaiable == 0:
        return print("This book has no copies avaiable at this moment")
    else:
        cursor.execute("INSERT INTO loans(user_id,book_id,loan_date) VALUES(%s,%s,%s) RETURNING loan_id",(user_id,book_id, datetime.datetime.now()))
        loan_id = cursor.fetchone()[0]
        cursor.execute("UPDATE books SET copies_avaiable = copies_avaiable - 1 WHERE book_id = %s",(book_id,))
        cursor.execute("UPDATE users SET last_login = %s WHERE user_id = %s" , (datetime.datetime.now(),user_id))
        conn.commit()
        return print(f"Loan made with loan_id = {loan_id}")
    
def return_book(loan_id):
    cursor.execute("SELECT user_id,book_id FROM loans WHERE loan_id = %s", (loan_id,))
    loan_data = cursor.fetchone()
    user_id = loan_data[0]
    book_id = loan_data[1]
    cursor.execute("UPDATE users SET last_login = %s WHERE user_id = %s" , (datetime.datetime.now(),user_id))
    cursor.execute("UPDATE books SET copies_avaiable = copies_avaiable + 1 WHERE book_id = %s" , (book_id,))
    cursor.execute("UPDATE loans SET return_date = %s WHERE loan_id = %s" , (datetime.datetime.now(),loan_id))
    conn.commit()
    return print(f"Book returned successfully")

return_book(4)