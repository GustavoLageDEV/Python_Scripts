# LIBRARY MANAGMENT SISTEM
# SIMPLE SISTEM TO MANAGE LOAN FROM A LIBRARY
# FUNCIONATIES: 1 - REGISTER USERS AND BOOKS (FUNCTIONS READY)
#               2 - REGISTER AND MANAGMENT OF LOANS 
#               3 - REPORTS (MOST POPULAR BOOKS, USER WITH MOST LOANS,...)
#               4 - INTERFACE


import psycopg2 as pg2
import datetime 

# Conexão com o banco de dados
conn = pg2.connect(dbname="mylibrary_project", user="postgres", password="373500")

cursor = conn.cursor()

def add_user(first_name,last_name,email):
    
    cursor.execute("INSERT INTO users(first_name,last_name,email) VALUES(%s,%s,%s) RETURNING user_id", (first_name,last_name,email))
    conn.commit()
    return cursor.fetchone()[0]

def add_book(title,author):
    
    cursor.execute("INSERT INTO books(title,author) VALUES(%s,%s) RETURNING book_id", (title,author))
    conn.commit()
    return cursor.fetchone()[0]

def book_loan(user_id,book_id):

    cursor.execute("SELECT copies_avaiable FROM books WHERE book_id = %s", user_id)
    cursor.execute("INSERT INTO loans(loan_id) VALUES(%s) RETURNING loan_id", datetime.datetime.now())
    conn.commit()
    return cursor.fetchone()[0]

#add_book("Memórias Póstumas de Brás Cubas","Machado de Assis")

print(cursor.execute("SELECT copies_avaiable FROM books WHERE book_id = 1"))