from task import Task
from repository import JsonRepository
import time


class TaskManager:
    def __init__(self):
        self.repository = JsonRepository()

    def interpreter(self, command):
        if not command:
            print("Debes introducir un comando.")
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
        else:
            print("No operation was performed.")

    def truncate_text(self, text, limit=20):
        text = str(text)

        if limit <= 3:
            return "." * limit

        if len(text) > limit:
            return text[:limit - 3] + "... "

        return text

    def new(self, *command):
        pass

    def show(self):
        data = self.repository.read_json()

        if data is None:
            print("No se pudieron leer las tareas.")
            return

        tasks = data.get("tasks", [])

        if not tasks:
            print("No hay tareas pendientes.")
            return

        print("\n╔═════════════════════════════════════╗")
        print("║ TASKS                               ║")

        for task in tasks:
            task_id = task.get("id", "?")
            name = self.truncate_text(
                task.get("name", "Sin nombre"), 30
            )

            print("╠═════════════════════════════════════╝")
            print(f"║ Task: #{task_id}")
            print(f"║ Name: {name}")
            

        print("╚═════════════════════════════════════╝\n")

    def update(self, *command):
        pass

    def delete(self, *command):
        pass