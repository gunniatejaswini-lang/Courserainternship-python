todo_list = []
def view_tasks():
    if not todo_list:
        print("\nYour to-do list is empty.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
        print()
def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added successfully!\n")
def update_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter task number to update: "))
            if 1 <= task_num <= len(todo_list):
                new_task = input("Enter the new task: ")
                todo_list[task_num - 1] = new_task
                print("Task updated successfully!\n")
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Please enter a valid number.\n")
def delete_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(todo_list):
                deleted_task = todo_list.pop(task_num - 1)
                print(f"Task '{deleted_task}' deleted successfully!\n")
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Please enter a valid number.\n")
while True:
    print("----- To-Do List Menu -----")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 5.\n")
