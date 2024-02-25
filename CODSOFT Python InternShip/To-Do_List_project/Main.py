import To_Do_List


def main():
    todo_list = To_Do_List.ToDoList()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added.")
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.mark_as_completed(index)
        elif choice == '4':
            index = int(input("Enter the index of the task to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            print("Thank you for using To-Do List")
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
