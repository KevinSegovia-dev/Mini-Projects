from task import Task
from cli import CLI
from repository import JsonRepository
import time

class TaskManager:
    def __init__(self):
        #self.task = Task()
        self.repository = JsonRepository()
        self.cli = CLI()
        self.commands = self.cli.command()
        self.interpreter(self.commands)
    
    def interpreter(self, commands):
        if commands[0] == "new":
            self.new()
        elif commands[0] == "show":
            self.show()
        elif commands[0] == "update":
            self.update()
        elif commands[0] == "delete":
            self.delete()
        else:
            print("No operation was successfully completed.")
            
    def new(self):
        pass
    
    def show(self):
        print(self.repository.open_json())
    
    def update(self):
        pass
    
    def delete(self):
        pass