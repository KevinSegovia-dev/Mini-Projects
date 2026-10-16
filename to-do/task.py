class Task:
    def __init__(self, id, name, description, created_at, state):
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.state = state
        
    def __str__(self):
        return f"id = {self.id}\nname = {self.name}\ndescription = {self.description}\ncreate at = {self.created_at}\nstate = {self.state}"