from new_task import add_task
from remove_task import remove_task
from completed_task import completed_task
from task_list import list_tasks

import argparse

def main():

    parser = argparse.ArgumentParser(description="Tasks/To-Do List Management Tool")
    # Argument for adding a task with help.
    parser.add_argument('--new', nargs=2, metavar=('task_name', 'task_description'), help="Create a new task on the list")
    # Argument for removing a task with help.
    parser.add_argument('--remove', type=int, metavar='task_number', help="Remove a task from the To-Do List by using the Task Number assigned to it.")
    # Argument for setting the completion status of a task in the To-Do list with help.
    parser.add_argument('--complete', type=int, metavar='task_number', help="Set a task to completed by using the task number automatically assigned to it.")
    # Argument for displaying a list of all tasks with help.
    parser.add_argument('--list', action='store_true', help='Display a list of all the current tasks in the To-Do List')

    args = parser.parse_args()

    if args.new:
        add_task(args.new[0], args.new[1])
    elif args.remove:
        remove_task(args.remove)
    elif args.complete:
        completed_task(args.complete)
    elif args.list:
        list_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()