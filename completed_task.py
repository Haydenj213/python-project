import sqlite3

conn = sqlite3.connect('tasks.db')

cursor = conn.cursor()

#Set the task as completed by selecting the task by its automatically generated number, and this command will set the complete value to 1, or TRUE.
def completed_task(task_number):
    cursor.execute('''UPDATE todolist SET completed = 1 WHERE task_number = ?''', (task_number,))
    conn.commit()