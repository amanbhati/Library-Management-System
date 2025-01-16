import mysql.connector
from flask import Flask, request, jsonify

# Flask app setup
app = Flask(__name__)

# MySQL database setup
def init_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password='Aman@955',  # Replace with your MySQL password
            database='library'
        )
        cursor = conn.cursor()

        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS library")
        cursor.execute("USE library")

        # Create tables
        cursor.execute('''CREATE TABLE IF NOT EXISTS customers (  
                            id INT AUTO_INCREMENT PRIMARY KEY,  
                            name VARCHAR(255) NOT NULL,  
                            email VARCHAR(255) UNIQUE NOT NULL  
                         )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS books (  
                            id INT AUTO_INCREMENT PRIMARY KEY,  
                            title VARCHAR(255) NOT NULL,  
                            author VARCHAR(255) NOT NULL,  
                            available BOOLEAN DEFAULT TRUE  
                         )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS issued_books (  
                            id INT AUTO_INCREMENT PRIMARY KEY,  
                            customer_id INT NOT NULL,  
                            book_id INT NOT NULL,  
                            issue_date DATETIME NOT NULL,  
                            FOREIGN KEY(customer_id) REFERENCES customers(id),  
                            FOREIGN KEY(book_id) REFERENCES books(id)  
                         )''')
        conn.commit()
        print("Database and tables initialized successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conn.is_connected():
            conn.close()

init_db()

if __name__ == '__main__':
    app.run(debug=True)
