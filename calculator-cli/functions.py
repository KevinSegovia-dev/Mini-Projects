import math
from datetime import datetime
import os
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def addition():
    while True:
        try:
            number1 = float(input("First number: "))
            number2 = float(input("Second number: "))
            break
        except ValueError:
            print(Fore.RED + "[ERROR] You must enter a number.\n")
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")
    add_history(f"{number1} + {number2} = {result}")
    
def subtraction():
    while True:
        try:
            number1 = float(input("First number: "))
            number2 = float(input("Second number: "))
            break
        except ValueError:
            print(Fore.RED + "[ERROR] You must enter a number.\n")
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")
    add_history(f"{number1} - {number2} = {result}")
    
def multiplication():
    while True:
        try:
            number1 = float(input("First number: "))
            number2 = float(input("Second number: "))
            break
        except ValueError:
            print(Fore.RED + "[ERROR] You must enter a number.\n")
    result = number1 * number2
    print(f"{number1} x {number2} = {result}")
    add_history(f"{number1} x {number2} = {result}")
    
def division():
    while True:
        try:
            number1 = float(input("First number: "))
            number2 = float(input("Second number: "))

            result = number1 / number2
            break

        except ValueError:
            print(Fore.RED + "[ERROR] You must enter a number.\n")

        except ZeroDivisionError:
            print(Fore.RED + "[ERROR] You cannot divide by zero.\n")
    print(f"{number1} / {number2} = {result}")
    add_history(f"{number1} / {number2} = {result}")
    
def integer_division():
    while True:
        try:
            number1 = float(input("First number: "))
            number2 = float(input("Second number: "))
    
            result = number1 // number2
            break
        
        except ValueError:
            print(Fore.RED + "[ERROR] You must enter a number.\n")
    
        except ZeroDivisionError:
            print(Fore.RED + "[ERROR] You cannot divide by zero.\n")
    print(f"{number1} // {number2} = {result}")
    add_history(f"{number1} // {number2} = {result}")
    
def modulo():
    while True:
        try:
            number1 = float(input("First number: "))
            number2 = float(input("Second number: "))
            break
        except ValueError:
            print(Fore.RED + "[ERROR] You must enter a number.\n")
    result = number1 % number2
    print(f"{number1} % {number2} = {result}")
    add_history(f"{number1} % {number2} = {result}")
    
def power():
    while True:
        try:
            base = float(input("Base: "))
            exponent = float(input("Exponent: "))
            result = round(base ** exponent,10)
            break
        except ValueError:
            print(Fore.RED + "[ERROR] You must enter a number.\n")
        except OverflowError:
            print(Fore.RED + "[ERROR] The result is too large.\n")
    print(f"{base} ^ {exponent} = {result}")
    add_history(f"{base} ^ {exponent} = {result}")
    
def square_root():
    while True:
        try:
            number = float(input("Enter a number: "))
            break
        except ValueError:
            print(Fore.RED + "[ERROR] You must enter a number.\n")
    result = math.sqrt(number)
    print(f"√{number} = {result}")
    add_history(f"Square root of {number} = {result}")

path_history = Path(__file__).parent / "history.txt"
 
def history():
    if not path_history.exists():
        path_history.touch()
        
    with open(path_history, "r") as file:
        content = file.read()

        if content == "":
            print(Fore.CYAN + "[INFO] The history is empty.\n")
            print(Style.BRIGHT + "==========================")
        else:
            print(content)
            print(Style.BRIGHT + "==========================\n")
        
    while True:
        print("1) clear the history\n2) exit\n")
        try:
            operation = int(input(f"Choose an option:\n{Fore.MAGENTA}>>>{Fore.RESET} "))
        except ValueError:
            print(Fore.RED + f"[ERROR] You must enter a number.\n")
            continue
        if operation == 1:
            clear_history()
            print(Fore.GREEN + "\n[OK] The history was cleared.\n")
        if operation == 2:
            break
            

def add_history(operation):
    date = datetime.now().strftime("%d/%m/%Y")
    if not path_history.exists():
        path_history.touch()
        
    with open(path_history, "a") as file:
        file.write(f"[{date}] {operation}\n")
        
def clear_history():
    with open(path_history, "w") as file:
        file.write("")
        
def clear_terminal():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux and macOS
        os.system("clear")
