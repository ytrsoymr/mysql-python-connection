import mysql.connector

def get_connection():
    """Establish and return a connection to the MySQL server."""
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database_name"  # Optional for connection without DB selection
    )
    if connection.is_connected():
        print("Connected to MySQL Server")
    return connection
