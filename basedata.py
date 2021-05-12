import sqlite3

class SqlLiteDB:

    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()
    
    def add_users(self, id, user_id, username, firstname):
        with self.connection:
            self.cursor.execute(f"INSERT INTO users VALUES (?,?,?,?)",(id, user_id, username, firstname))
    
    def checking_users(self, user_id):
        with self.connection:
            self.cursor.execute("SELECT user_id FROM users WHERE user_id = ?",(user_id))
            result = self.cursor.fetchone()
            if result is None:
                return True
            else:
                return False
    
    def close(self):
        self.connection.close()