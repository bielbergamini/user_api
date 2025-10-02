import sqlite3

def create_connection():
    connection = sqlite3.connect("users.db") # open database
    return connection

def create_table():
    conn = create_connection()
    cursor = conn.cursor() # Exec commands SQL

    sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        birth_date TEXT
    )
"""

    cursor.execute(sql) # Exec sql
    conn.commit() # Save alterations
    conn.close() # Close connection



