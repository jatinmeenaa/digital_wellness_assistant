import mysql.connector
from mysql.connector import Error

def get_connection():
    """Create and return a MySQL database connection."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",       # Replace with your username
            password="your_password",   # Replace with your password
            database="digital_wellness",
            charset="utf8mb4",
            collation="utf8mb4_unicode_ci"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def close_connection(connection):
    """Close the given MySQL database connection."""
    if connection and connection.is_connected():
        connection.close()
