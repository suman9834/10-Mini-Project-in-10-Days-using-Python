tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_number = int(input("Enter task number to delete: "))

            if 1 <= task_number <= len(tasks):
                removed = tasks.pop(task_number - 1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice!")