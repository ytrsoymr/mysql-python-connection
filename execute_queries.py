from connect_mysql import get_connection

def insert_data(name, age):
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO my_table (name, age) VALUES (%s, %s)"
    cursor.execute(query, (name, age))
    connection.commit()
    print(f"Inserted {cursor.rowcount} row(s).")
    cursor.close()
    connection.close()

def fetch_data():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM my_table")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()

if __name__ == "__main__":
    insert_data("Alice", 25)
    fetch_data()
