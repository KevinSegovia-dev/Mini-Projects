import json
import datetime
import argparse


class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-new", "--new", nargs=2, metavar=("name", "description"), help="Create a new task with two arguments")

        self.parser.add_argument("-show", "--show", help="View all tasks")

        self.parser.add_argument("-update", "--update", type=int, help="ID of the task to edit")

        self.parser.add_argument("-name", "--name", type=str, help="New task name")
        self.parser.add_argument("-description", "--description", type=str, help="New task description")
        self.parser.add_argument("-status", "--status", choices=["not started", "in progress", "completed"], help="New task state")

        self.parser.add_argument("-delete", "--delete", type=int, help="Delete a task by ID")

    def command_new_task(self):
        self.args = self.parser.parse_args()
        if self.args.new:
            name, description = self.args.new

        return name, description

    def command_show_tasks(self):
        pass
    
    def command_update_task(self):
        self.args = self.parser.parse_args()

        id_task = self.args.update
        new_name = self.args.name
        new_description = self.args.description
        new_status = self.args.status

        if self.args.update and not (new_name, new_description, new_status):
            self.parser.error("-update requires at least 1 argument to change (-name, -description, etc.)")
            
        if new_name is None and new_description is None and new_status is None:
            self.parser.error("You must specify at least one field to edit (-name, -description, etc.)")
        
        return (id_task,new_name,new_description,new_status)
    
    def command_delete_task(self):
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
result = cli.command_update_task()
print(result)
