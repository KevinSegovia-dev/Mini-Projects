import sys

class Calculator:
    def __init__(self):
        self.interface()
    
    def addition(self):
        number1 = float(input("Primer numero: "))
        number2 = float(input("Segundo numero: "))
        print(number1 + number2)
    def subtraction(self):
        pass
    def multiplication(self):
        pass
    def division(self):
        pass
    def integer_division(self):
        pass
    def modulo(self):
        pass
    def power(self):
        pass
    def square_root(self):
        pass
    def historial(self):
        pass
    
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
     ██─██▀█─██─██─█─███─▄█▀█  ║ 9) Historial.                    ║
     ▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄█  ║ 11) exit.                        ║
                               ╚══════════════════════════════════╝
        """
        print(menu)
        
        operation = int(input("Elige una operacion:\n>>> "))
        
        if operation == 1:
            self.addiction()
        elif operation == 2:
            self.subtraction()
        elif operation == 3:
            self.multiplication()
        elif operation == 4:
            self.division()
        elif operation == 5:
            self.integer_division()
        elif operation == 6:
            self.modulo()
        elif operation == 7:
            self.power()
        elif operation == 8:
            self.square_root()
        elif operation == 9:
            self.historial()
        elif operation == 11:
            sys.exit()
        else:
            operation = int(input("Elige una operacion:\n>>> "))