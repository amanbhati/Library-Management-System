import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime

st.title("Library Management System")

# MySQL database connection
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',  # MySQL server host
            user='root',  # MySQL username
            password='Aman@955',  # MySQL password
            database='library'  # Database name
        )
        return conn
    except Error as e:
        st.error(f"Error: {e}")
        return None

# Add a new user

st.header("Add a New User")
new_user_name = st.text_input("Name", key="user_name_1")  # unique key for this instance
new_user_email = st.text_input("Email", key="user_email_1")  # unique key for this instance
if st.button("Add User"):
    if new_user_name and new_user_email:
        try:
            conn = get_db_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO customers (name, email) VALUES (%s, %s)", (new_user_name, new_user_email))
                conn.commit()
                conn.close()
                st.success(f"User {new_user_name} added successfully!")
                # Reset the fields
                st.text_input("Name", key="user_name_1", value="")
                st.text_input("Email", key="user_email_1", value="")
                st.experimental_rerun()
        except mysql.connector.IntegrityError:
            st.error("Email already exists.")
        except Error as e:
            st.error(f"Error: {e}")
    else:
        st.error("Please fill out both fields.")

# Add a new book
st.header("Add a New Book")
new_book_title = st.text_input("Book Title", key="book_title")
new_book_author = st.text_input("Author", key="book_author")
if st.button("Add Book"):
    if new_book_title and new_book_author:
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (new_book_title, new_book_author))
            conn.commit()
            conn.close()
            st.success(f"Book '{new_book_title}' by {new_book_author} added successfully!")
            # Reset the fields
            st.text_input("Book Title", key="book_title", value="")
            st.text_input("Author", key="book_author", value="")
            st.experimental_rerun()
        else:
            st.error("Failed to connect to database.")
    else:
        st.error("Please fill out both fields.")

# Count the number of books in the library
st.header("Total Books in Library")
conn = get_db_connection()
if conn:
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM books")
    book_count = cursor.fetchone()[0]
    conn.close()
    st.write(f"Total books in the library: {book_count}")
else:
    st.error("Failed to fetch book count.")

# Issue a book
st.header("Issue a Book")
issue_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Fetch available books and customers for issuing
conn = get_db_connection()
if conn:
    cursor = conn.cursor()

    # Fetch customers
    cursor.execute("SELECT id, name FROM customers")
    customers = cursor.fetchall()

    # Search for customer functionality
    search_query_customer = st.text_input("Search for a Customer (by Name)", key="search_customer")
    
    # Filter customers based on the search query
    if search_query_customer:
        filtered_customers = [customer for customer in customers if search_query_customer.lower() in customer[1].lower()]
    else:
        filtered_customers = customers
    
    # Display the filtered customer options
    customer_options = [customer[1] for customer in filtered_customers]
    customer_id = st.selectbox("Select Customer", customer_options)

    # Fetch books
    search_query_book = st.text_input("Search for a Book (by Title)", key="search_book")

    # Filter books based on the search query
    cursor.execute("SELECT id, title FROM books WHERE available = TRUE")
    books = cursor.fetchall()
    filtered_books = [book for book in books if search_query_book.lower() in book[1].lower()] if search_query_book else books
    book_options = [book[1] for book in filtered_books]
    book_id = st.selectbox("Select Book", book_options)

    # Issue the book
    if st.button("Issue Book"):
        if customer_id and book_id:
            try:
                # Get customer and book IDs
                customer_id = [customer[0] for customer in customers if customer[1] == customer_id][0]
                book_id = [book[0] for book in filtered_books if book[1] == book_id][0]

                cursor.execute("INSERT INTO issued_books (customer_id, book_id, issue_date) VALUES (%s, %s, %s)", 
                               (customer_id, book_id, issue_date))
                cursor.execute("UPDATE books SET available = FALSE WHERE id = %s", (book_id,))
                conn.commit()
                st.success(f"Book '{book_id}' issued successfully to {customer_id}!")
                # Reset the selection after issuing
                st.session_state.customer_id = None
                st.session_state.book_id = None
                # Reset the widgets to empty state
                st.experimental_rerun()
            except Error as e:
                st.error(f"Error: {e}")
            finally:
                conn.close()
        else:
            st.error("Please select both customer and book.")
else:
    st.error("Failed to fetch data for issuing books.")

# View issued books history
st.header("Issued Books History")
conn = get_db_connection()
if conn:
    cursor = conn.cursor()
    cursor.execute('''SELECT books.title, books.author, customers.name, issued_books.issue_date 
                      FROM issued_books 
                      JOIN books ON issued_books.book_id = books.id 
                      JOIN customers ON issued_books.customer_id = customers.id''')
    issued_books = cursor.fetchall()
    conn.close()

    if issued_books:
        for record in issued_books:
            book_title, book_author, customer_name, issue_date = record
            st.write(f"Book: {book_title} | Author: {book_author} | Issued to: {customer_name} | Date: {issue_date}")
    else:
        st.write("No books have been issued yet.")
else:
    st.error("Failed to fetch data from the database.")
