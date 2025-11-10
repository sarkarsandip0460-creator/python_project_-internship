from task_manager_app.task import Task
from task_manager_app.file_handler import read_tasks, write_tasks
from task_manager_app.input_validator import get_valid_string, get_valid_priority

TASKS_FILE = "data/tasks.json"

def main_menu():
    print("\n---------------------------")
    print("     TASK MANAGER APP      ")
    print("---------------------------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("---------------------------")

def add_task(tasks):
    title = get_valid_string("Enter task title: ")
    description = get_valid_string("Enter task description: ")
    priority = get_valid_priority()
    new_task = Task(title, description, priority)
    tasks.append(new_task)
    write_tasks(TASKS_FILE, tasks)
    print("✅ Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task.title} ({task.priority}) - {task.description}")
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            write_tasks(TASKS_FILE, tasks)
            print(f"🗑 Deleted: {removed.title}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def run_app():
    print("🚀 Task Manager App started!")
    tasks = read_tasks(TASKS_FILE)
    while True:
        main_menu()
        choice = input("Enter your choice: ").strip()
        if choice == '1':
         add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("👋 Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")
            
if __name__=="__main__":
    run_app()
    
    