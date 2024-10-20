
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"Task: {self.description} | Status: {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    #  to add a new task
    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task '{description}' added successfully!")

    #  to view all tasks
    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    #  to update a task's description
    def update_task(self, task_number, new_description):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].description = new_description
            print(f"Task {task_number} updated successfully!")
        else:
            print("Invalid task number.")

    #  to mark a task as completed
    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_complete()
            print(f"Task {task_number} marked as completed!")
        else:
            print("Invalid task number.")

    #  to delete a task
    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"Task '{deleted_task.description}' deleted successfully!")
        else:
            print("Invalid task number.")


#   to run the to-do list
def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            task_number = int(input("Enter task number to update: "))
            new_description = input("Enter new task description: ")
            todo_list.update_task(task_number, new_description)

        elif choice == '4':
            task_number = int(input("Enter task number to mark as complete: "))
            todo_list.complete_task(task_number)

        elif choice == '5':
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)

        elif choice == '6':
            print("Exiting To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
