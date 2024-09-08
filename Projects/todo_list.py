# todo_list.py

import os

# File to store tasks
TASKS_FILE = 'tasks.txt'

def load_tasks():
    """Load tasks from the file."""
    if not os.path.isfile(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(tasks):
    """Add a new task."""
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added.")

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks to display.")
    else:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def remove_task(tasks):
    """Remove a task."""
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
