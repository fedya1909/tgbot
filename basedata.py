import sqlite3

class SqlLiteDB:


    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file, check_same_thread = False)
        self.cursor = self.connection.cursor()
    
    def create_table(self):
        return self.cursor.execute('CREATE TABLE IF NOT EXISTS users (userID integer primary key)')
        
    def add_users(self, user_id):
        self.create_table()
        with self.connection:
            return self.cursor.execute("INSERT OR REPLACE INTO 'users' VALUES (?)",(user_id,))
    
    def checking_users(self, user_id):
        self.create_table()
        with self.connection:
            result = self.cursor.execute("SELECT 'userID' FROM 'users' WHERE 'userID' = ?",(user_id,)).fetchall()
            return bool(len(result))
    
    def close(self):
        self.connection.close()