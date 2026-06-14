def show_menu():
    print("\n==== TO-DO LIST APP ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Exit")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task['done'] else "❌"
            print(f"{i}. {task['title']} - {status}")

def add_task(tasks):
    title = input("Enter a new task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print("Task added!")
    else:
        print("Task cannot be empty.")

def mark_task_done(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            choice = int(input("Enter task number to mark as done: "))
            if 1 <= choice <= len(tasks):
                tasks[choice - 1]['done'] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
