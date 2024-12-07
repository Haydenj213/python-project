import sqlite3

conn = sqlite3.connect('tasks.db')

cursor = conn.cursor()

#Arg/Function that will remove the task by the task number assigned automatically.
def remove_task(task_number):
    cursor.execute('''DELETE FROM todolist WHERE task_number = ?''', (task_number, ))
    conn.commit()
