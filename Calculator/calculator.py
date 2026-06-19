import sys

class Calculator:
    def __init__(self, procesador):
        self.interface()
        self.procesador = procesador
    
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
            self.procesador.addiction()
        elif operation == 2:
            self.procesador.subtraction()
        elif operation == 3:
            self.procesador.multiplication()
        elif operation == 4:
            self.procesador.division()
        elif operation == 5:
            self.procesador.integer_division()
        elif operation == 6:
            self.procesador.modulo()
        elif operation == 7:
            self.procesador.power()
        elif operation == 8:
            self.procesador.square_root()
        elif operation == 9:
            self.procesador.historial()
        elif operation == 11:
            sys.exit()
        else:
            operation = int(input("Elige una operacion:\n>>> "))