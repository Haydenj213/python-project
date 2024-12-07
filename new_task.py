import sqlite3

conn = sqlite3.connect('tasks.db')

cursor = conn.cursor()

#Add task arg/function where you add the task name, description, and the completed value is automatically set to false. Task number is automatically assigned as well.
def add_task(task_name, task_description):
    cursor.execute('''INSERT INTO todolist (task_name, task_description, completed) VALUES (?, ?, 0)''', (task_name, task_description))
    conn.commit()