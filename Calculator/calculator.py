import math

class Calculator:
    def __init__(self):
        self.interface()
    
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
                               ║ 6) modulo or remainder.          ║
     ████████████████████████  ║ 7) power.                        ║
     █▄─▄███─▄▄─█▄─█─▄█▄─▄▄─█  ║ 8) Square root.                  ║
     ██─██▀█─██─██─█─███─▄█▀█  ║ 9) Historial.                    ║
     ▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄█  ║ 11) exit.                        ║
                               ╚══════════════════════════════════╝
        """
        print(menu)