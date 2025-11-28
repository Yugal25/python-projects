tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    print("\n1. Add Task\n2. Show Tasks\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
1