import sqlite3
from app.database import create_connection
from app.models import User


class UserRepository():
    def __init__(self):
        pass


    def add_user(self, user: User):
        
        conn = create_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO users (name, email, password, birth_date)
        VALUES (?, ?, ?, ?)
        """
        
        try:
            cursor.execute(sql, (user.name, user.email, user.password, user.birth_date))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            print(f"Error: user with email {user.email} already exists.")
            return False
        finally: 
            conn.close()
