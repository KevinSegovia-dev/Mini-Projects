import json
import datetime
import argparse


class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-new", "--new", nargs=2, metavar=("name", "description"), help="Create a new task with two arguments")
        
        self.parser.add_argument("-show", "--show", help="View all tasks")
        
        self.parser.add_argument("-uptade", "--uptade", type=int, help="ID of the task to edit")
        
        self.parser.add_argument("-name", "--name", type=str, help="New task name")
        self.parser.add_argument("-description", "--description", type=str, help="New task description")
        self.parser.add_argument("-status", "--status", choices=["not started", "in progress", "completed"], help="New task state")
        
        self.parser.add_argument("-delete", "--delete", type=int, help="Delete a task by ID")

    def new_task(self):
        self.args = self.parser.parse_args()
        if self.args.new:
            name, description = self.args.new
            
        return name, description
    
    def show_tasks(self):
        pass
    
    def edit_tasks(self):
        self.args = self.parser.parse_args()
        
        if self.args.uptade and not (self.args.description,self.args.name,self.args.status):
            self.parser.error("-edit requires at least 1 argument to change (-name, -description, etc.)")
            
        if self.args.name is None and self.args.description is None and self.args.status is None:
            self.parser.error("You must specify at least one field to edit (-name, -description, etc.)")
        
        return "Successful action"
    
    def delete_tasks(self):
        pass

class TaskManager:
    def __init__(self):
        pass

class Task:
    def __init__(self,id,name,description,created_at,state):
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.state = state


class JsonRepository:
    def __init__(self):
        pass

cli = CLI()
result = cli.edit_tasks()
print(result)