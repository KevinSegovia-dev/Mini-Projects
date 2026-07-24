import math
from datetime import datetime
import os
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def addition():
    while True:
        try:
            number1 = float(input("Primer número: "))
            number2 = float(input("Segundo número: "))
            break
        except ValueError:
            print(Fore.RED + "[ERROR] Debes escribir un número.\n")
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")
    add_historial(f"{number1} + {number2} = {result}")
    
def subtraction():
    while True:
        try:
            number1 = float(input("Primer numero: "))
            number2 = float(input("Segundo numero: "))
            break
        except ValueError:
            print(Fore.RED + "[ERROR] Debes escribir un número.\n")
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")
    add_historial(f"{number1} - {number2} = {result}")
    
def multiplication():
    while True:
        try:
            number1 = float(input("Primer numero: "))
            number2 = float(input("Segundo numero: "))
            break
        except ValueError:
            print(Fore.RED + "[ERROR] Debes escribir un número.\n")
    result = number1 * number2
    print(f"{number1} x {number2} = {result}")
    add_historial(f"{number1} x {number2} = {result}")
    
def division():
    while True:
        try:
            number1 = float(input("Primer número: "))
            number2 = float(input("Segundo número: "))

            result = number1 / number2
            break

        except ValueError:
            print(Fore.RED + "[ERROR] Debes escribir un número válido.\n")

        except ZeroDivisionError:
            print(Fore.RED + "[ERROR] No se puede dividir entre cero.\n")
    print(f"{number1} / {number2} = {result}")
    add_historial(f"{number1} / {number2} = {result}")
    
def integer_division():
    while True:
        try:
            number1 = float(input("Primer número: "))
            number2 = float(input("Segundo número: "))
    
            result = number1 // number2
            break
        
        except ValueError:
            print(Fore.RED + "[ERROR] Debes escribir un número válido.\n")
    
        except ZeroDivisionError:
            print(Fore.RED + "[ERROR] No se puede dividir entre cero.\n")
    print(f"{number1} // {number2} = {result}")
    add_historial(f"{number1} // {number2} = {result}")
    
def modulo():
    while True:
        try:
            number1 = float(input("Primer numero: "))
            number2 = float(input("Segundo numero: "))
            break
        except ValueError:
            print(Fore.RED + "[ERROR] Debes escribir un número.\n")
    result = number1 % number2
    print(f"{number1} % {number2} = {result}")
    add_historial(f"{number1} % {number2} = {result}")
    
def power():
    while True:
        try:
            base = float(input("Base: "))
            exponente = float(input("Exponente: "))
            result = round(base ** exponente,10)
            break
        except ValueError:
            print(Fore.RED + "[ERROR] Debes escribir un número.\n")
        except OverflowError:
            print(Fore.RED + "[ERROR] El resultado es demasiado grande.\n")
    print(f"{base} ^ {exponente} = {result}")
    add_historial(f"{base} ^ {exponente} = {result}")
    
def square_root():
    while True:
        try:
            number = float(input("ingrese un numero: "))
            break
        except ValueError:
            print(Fore.RED + "[ERROR] Debes escribir un número.\n")
    result = math.sqrt(number)
    print(f"√{number} = {result}")
    add_historial(f"Square root of {number} = {result}")

path_historial = Path(__file__).parent / "historial.txt"
 
def historial():
    if not path_historial.exists():
        path_historial.touch()
        
    with open(path_historial, "r") as file:
        content = file.read()

        if content == "":
            print(Fore.CYAN + "[INFO] El historial está vacío.\n")
            print(Style.BRIGHT + "==========================")
        else:
            print(content)
            print(Style.BRIGHT + "==========================\n")
        
    while True:
        print("1) clear the history\n2) exit\n")
        try:
            operation = int(input(f"Elige una opcion:\n{Fore.MAGENTA}>>>{Fore.RESET} "))
        except ValueError as e:
            print(Fore.RED + f"[ERROR] {e}\n")
            continue
        if operation == 1:
            clear_historial()
            print(Fore.GREEN + "\n[OK] The history was cleared.\n")
        if operation == 2:
            break
            

def add_historial(operation):
    fecha = datetime.now().strftime("%d/%m/%Y")
    if not path_historial.exists():
        path_historial.touch()
        
    with open(path_historial, "a") as file:
        file.write(f"[{fecha}] {operation}\n")
        
def clear_historial():
    with open(path_historial, "w") as file:
        file.write("")
        
def clear_terminal():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux y macOS
        os.system("clear")