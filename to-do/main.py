from manager import TaskManager
from cli import CLI

if __name__ == '__main__':
    cli = CLI()
    commands = cli.command()
    
    manager = TaskManager()
    manager.interpreter(commands)