import argparse

class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        
        self.parser.add_argument("-new", "--new", nargs="+", metavar=("name", "description"), help="Create a new task with two arguments")

        self.parser.add_argument("-show", "--show", action='store_true', help="View all tasks")

        self.parser.add_argument("-update", "--update", type=int, help="ID of the task to edit")

        self.parser.add_argument("-name", "--name", type=str, help="New task name")
        self.parser.add_argument("-description", "--description", type=str, help="New task description")
        self.parser.add_argument("-status", "--status", choices=["not-started", "in-progress", "completed"], help="New task state")

        self.parser.add_argument("-delete", "--delete", type=int, help="Delete a task by ID")

    def command(self):
        self.args = self.parser.parse_args()
        
        id_task = self.args.update
        new_name = self.args.name
        new_description = self.args.description
        new_status = self.args.status
        
        if self.args.new:
            if len(self.args.new) == 1:
                name = self.args.new[0]
                description = None
                return ("new", name, description)
            elif len(self.args.new) == 2:
                name, description = self.args.new
                return ("new", name, description)
            else:
                self.parser.error("The -new argument requires a maximum of 2 values ​​(name and description).")
        
        if self.args.show:
            return ("show",)
        
        if self.args.update:
            if self.args.update and not (new_name, new_description, new_status):
                self.parser.error("-update requires at least 1 argument to change (-name, -description, -status)")

            if new_name is None and new_description is None and new_status is None:
                self.parser.error("You must specify at least one field to edit (-name, -description, -status)")

            return ("update", id_task,new_name,new_description,new_status)

        if self.args.delete:
            return ("delete", self.args.delete)