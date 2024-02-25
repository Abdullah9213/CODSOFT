class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start = 1):
                status="✔" if task['completed'] else ' '
                print(f"{index}. {status} - {task['task']}")

    def mark_as_completed(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index-1]
            print("Task deleted.")
        else:
            print("Invalid task index.")


