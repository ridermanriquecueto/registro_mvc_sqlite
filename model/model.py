import sqlite3

class UserModel:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        ''')
        self.connection.commit()

    def insert_user(self, name, email):
        self.cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        self.connection.commit()

    def get_users(self):
        self.cursor.execute('SELECT id, name, email FROM users')
        return self.cursor.fetchall()

    def update_user(self, user_id, new_name):
        self.cursor.execute('UPDATE users SET name = ? WHERE id = ?', (new_name, user_id))
        self.connection.commit()

    def delete_user(self, user_id):
        self.cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
