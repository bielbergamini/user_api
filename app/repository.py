import sqlite3
from app.database import create_connection
from app.models import User
from typing import Optional


class UserRepository():
    def __init__(self):
        pass


    def add_user(self, user: User):
        
        conn = create_connection() # returns a connection to the SQLite database
        cursor = conn.cursor() # Cursor exec SQL commands
   
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

        
    def get_all_users(self):
        users = []
        conn = create_connection()
        cursor = conn.cursor()
        

        sql = """
        SELECT * FROM users
        """
        

        cursor.execute(sql)
        rows = cursor.fetchall()
        
        for row in rows:
            user = User(id= row[0], name= row[1], email= row[2], password= row[3], birth_date= row[4])
            users.append(user)

        return users

        
    
                                            #(X or None)
    def get_user_by_id(self, user_id: int) -> Optional[User]:

        conn = create_connection()
        cursor = conn.cursor()

        sql = """
        SELECT * FROM users WHERE id = ?
        """
            
        cursor.execute(sql, (user_id,))
        row = cursor.fetchone()

        if row is None:
            return None
        else:
            user = User(id= row[0], name= row[1], email= row[2], password= row[3], birth_date= row[4])
            return user
        

    def update_user(self, user: User):

        conn = create_connection()
        cursor = conn.cursor()

        sql = """
        UPDATE users
        SET name = ?, email = ?, password = ?, birth_date = ?
        WHERE id = ?
        """
         
        cursor.execute(sql, (user.name, user.email, user.password, user.birth_date, user.id))
        updated_rows = cursor.rowcount

        if updated_rows == 0:
            conn.close()
            return False
        else:
            conn.commit()
            conn.close()
            return True
        
        
        
        
