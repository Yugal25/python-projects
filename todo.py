tasks = []

def show_tasks():
    if len(tasks) == 0:       # if not tasks:
        print("No tasks yet")
    else:
        print('\n The tasks list is as follows: \n')
        i = 1
        for task in tasks:
            print(i, task )
            i += 1


while True:
    print("\n 1. Add Task \n2. Show Tasks \n3. Exit")

    choice = input("Enter your choice: ")

    if choice =="1":
        tasks.append(input("Enter new task: "))
        print("Task added succesfully.")

    elif choice =="2":
        show_tasks()

    elif choice =="3":
        print("You chose to exit...")
        break

    else:
        print("Invalid choice")

