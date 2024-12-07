import sqlite3

conn = sqlite3.connect('tasks.db')

cursor = conn.cursor()

#Simple arg/function that will display a list of all the tasks/display the full table.
def list_tasks():
    cursor.execute("SELECT * FROM todolist")
    tasks = cursor.fetchall()
    for task in tasks:
        status = 'Completed' if task[3] else 'Pending'
        print (f"Task Number: {task[0]}, Task Name: {task[1]}, Task Description: {task[2]}, Completed?: {status}")