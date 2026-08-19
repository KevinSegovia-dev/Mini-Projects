import json
import datetime
import argparse


class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--new", action="store_true", help="Create a new task")
        self.parser.add_argument("-name", type=str, help="Give the task a name")
        self.parser.add_argument("-description", type=str, help="Give the task a description")

    def print_text(self):
        self.args = self.parser.parse_args()
        name = self.args.name
        description = self.args.description
        
        if self.args.new and not self.args.name:
             return self.parser.error("--new requires -name")
         
        if not self.args.new and (self.args.name or self.args.description):
            return self.parser.error("-name and -description require --new")

        return f"Name: {name}\nDescription: {description}"
    
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
result = cli.print_text()
print(result)