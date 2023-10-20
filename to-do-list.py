todo_list = []

def add_task(task):
    todo_list.append(task)

def list_tasks():
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

def remove_task(task_index):
    if task_index >= 1 and task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Removed: {removed_task}")
    else:
        print("Invalid task index")

# Main loop to interact with the user
while True:
    print("\nTo-Do List:")
    list_tasks()
    print("\nMenu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Quit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        task_index = int(input("Enter the task number to remove: "))
        remove_task(task_index)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
