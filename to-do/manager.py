from task import Task
from repository import JsonRepository
import time


class TaskManager:
    def __init__(self):
        self.repository = JsonRepository()
        
    def interpreter(self, command):
        if not command:
            print("You must enter a command.")
            return

        operation = command[0]

        if operation == "new":
            print(self.new(*command))
        elif operation == "show":
            self.show()
        elif operation == "update":
            print(self.update(*command))
        elif operation == "delete":
            print(self.delete(*command))
        elif operation == "view":
            print(self.view_tasks(*command))
        else:
            print("No operation was performed.")
            
    def truncate_text(self, text, limit=20):
        text = str(text)

        if limit <= 3:
            return "." * limit

        if len(text) > limit:
            return text[:limit - 3] + "..."

        return text

    #=====================================================
    
    def new(self, *command):
        pass

    def show(self):
        data = self.repository.read_json()

        if data is None:
            print("The tasks could not be read.")
            return

        tasks = data.get("tasks", [])

        if not tasks:
            print("There are no pending tasks.")
            return

        print("\n╔═════════════════════════════════════╗")
        print("║ TASKS                               ║")
        print("╚═════════════════════════════════════╝")

        for task in tasks:
            task_id = task.get("id", "?")
            name = self.truncate_text(
                task.get("name", "Unnamed"), 30
            )

            print(f"  Task: #{task_id}")
            print(f"  Name: {name}")
            print("═══════════════════════════════════════")
        print()

    def update(self, *command):
        pass

    def delete(self, *command):
        pass
    
    def view_tasks(self, *command):
        data = self.repository.read_json()

        if data is None:
            print("The tasks could not be read.")
            return

        tasks = data.get("tasks", [])

        if not tasks:
            print("There are no pending tasks.")
            return
        
        for task in tasks:
            task_description = task.get("description", "?")
            
        while True:
            operation = int(input("Choose an option: "))
            
            if operation == 1:
                return task_description
            elif operation == 2:
                break
            else:
                return "Choose a valid option."