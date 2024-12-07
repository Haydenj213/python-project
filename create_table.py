import sqlite3 

conn = sqlite3.connect('tasks.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS todolist (
                    task_number INTEGER PRIMARY KEY,
                    task_name TEXT,
                    task_description TEXT,
                    completed INTEGER NOT NULL CHECK (completed IN (0, 1))
               )''')
conn.commit()