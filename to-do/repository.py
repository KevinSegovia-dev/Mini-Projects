import json

class JsonRepository:
    def __init__(self):
        pass
    
    def write_json(self,data):
        with open("tasks.json", "w", encoding="utf-8") as file:
            pass
        
    def read_json(self):
        try:
            with open("tasks.json", "r", encoding="utf-8") as file:
                tasks = json.load(file)
                return tasks
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error al leer el archivo JSON: {e}")
        return None