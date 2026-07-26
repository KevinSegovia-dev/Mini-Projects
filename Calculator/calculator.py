import sys
import time
from functions import *
from colorama import Fore, Back, Style, init

init(autoreset=True)

class Calculator:
    def __init__(self):
        self.interface()
        self.clear_terminal()
    
    def interface(self):
        menu = """
         ███   ███  █      ███  █   █ █      ███  █████  ███  ████  
        █     █   █ █     █     █   █ █     █   █   █   █   █ █   █ 
        █     █████ █     █     █   █ █     █████   █   █   █ ████  
        █     █   █ █     █     █   █ █     █   █   █   █   █ █  █  
         ███  █   █ █████  ███   ███  █████ █   █   █    ███  █   █
        
                               ╔═══════════ Operations ═══════════╗
            ─▄▀─▄▀             ║ 1) Addition.                     ║
            ──▀──▀             ║ 2) Subtraction.                  ║
            █▀▀▀▀▀█▄           ║ 3) Multiplication.               ║
            █░░░░░█─█          ║ 4) Division.                     ║
            ▀▄▄▄▄▄▀▀           ║ 5) Integer division.             ║
                               ║ 6) Modulo or remainder.          ║
     ████████████████████████  ║ 7) Power.                        ║
     █▄─▄███─▄▄─█▄─█─▄█▄─▄▄─█  ║ 8) Square root.                  ║
     ██─██▀█─██─██─█─███─▄█▀█  ║ 9) History.                      ║
     ▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄█  ║ 10) exit.                        ║ 
                               ╚══════════════════════════════════╝
        """
        while True:
            try:
                print(menu)
                operation = int(input(f"Choose an operation:\n{Fore.MAGENTA}>>>{Fore.RESET} "))
            except ValueError:
                print(Fore.RED + f"[ERROR] You must enter a number.")
            clear_terminal()
            
            if operation == 1:
                print(f"{Style.BRIGHT}=== Addition ==={Fore.RESET}\n")
                addition()
                
            elif operation == 2:
                print(f"{Style.BRIGHT}=== Subtraction ==={Fore.RESET}\n")
                subtraction()

            elif operation == 3:
                print(f"{Style.BRIGHT}=== Multiplication ==={Fore.RESET}\n")
                multiplication()

            elif operation == 4:
                print(f"{Style.BRIGHT}=== Division ==={Fore.RESET}\n")
                division()

            elif operation == 5:
                print(f"{Style.BRIGHT}=== Integer division ==={Fore.RESET}\n")
                integer_division()

            elif operation == 6:
                print(f"{Style.BRIGHT}=== Modulo ==={Fore.RESET}\n")
                modulo()

            elif operation == 7:
                print(f"{Style.BRIGHT}=== Power ==={Fore.RESET}\n")
                power()

            elif operation == 8:
                print(f"{Style.BRIGHT}=== Square root ==={Fore.RESET}\n")
                square_root()

            elif operation == 9:
                print(f"{Style.BRIGHT}======= Historial ========{Fore.RESET}\n")
                history()

            elif operation == 10:
                print("\nClosing the system...")
                time.sleep(1)
                print("See you later!\n")
                sys.exit()
                
            else:
                try:
                    print(menu)
                    operation = int(input(f"Choose an operation:\n{Fore.MAGENTA}>>>{Fore.RESET} "))
                except ValueError:
                    print(Fore.RED + f"[ERROR] You must enter a number.")
                clear_terminal()
