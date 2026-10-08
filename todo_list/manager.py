from task import Task
from cli import CLI
import time

class TaskManager:
    def __init__(self):
        #self.task = Task()
        self.cli = CLI()
        self.commands = self.cli.command()
        self.interpreter(self.commands)
    
    def interpreter(self,commands):
        if commands:
            print(commands)
    
    def new(self):
        pass
    
    def show(self):
        pass
    
    def update(self):
        pass
    
    def delete(self):
        pass