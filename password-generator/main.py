import os, random, time
from colorama import Fore, init
import string

init(autoreset=True)

class PasswordGenerator:
    def __init__(self):
        self.run()
        
    def run(self):
        while True:
            length = input(f"\nEnter a length or 'exit' to quit:\n{Fore.MAGENTA}>>>{Fore.RESET} ")
            if length == 'exit':
                self.clear_terminal()
                print("\nClosing the system...")
                time.sleep(1.5)
                self.clear_terminal()
                break
            try:
                self.clear_terminal()
                number_length = int(length)
                if number_length > 15 or number_length < 1:
                    print(Fore.RED + f"\n[ERROR] The number is too long.")
                else:
                    print(self.generator(number_length))
            except ValueError:
                print(Fore.RED + f"\n[ERROR] Enter a number or 'exit' to quit.")
    
    def secure_password_detector(self, length):
        levels = ['Very Weak', 'Weak', 'Good', 'Strong']

        if length <= 4:
            return f"Password security level:\n{Fore.RED}{levels[0]}{Fore.RESET}"    # Very Weak (1-4)
        elif length <= 8:
            return f"Password security level:\n{Fore.YELLOW}{levels[1]}{Fore.RESET}"    # Weak (5-8)
        elif length <= 12:
            return f"Password security level:\n{Fore.GREEN}{levels[2]}{Fore.RESET}"    # Good (9-12)
        else:
            return f"Password security level:\n{Fore.BLUE}{levels[3]}{Fore.RESET}"    # Strong (13 a 15+)
        
    def generator(self, length):
        simbols = string.punctuation
        numbers = string.digits
        letters = string.ascii_letters
        random_letters = simbols + letters + numbers 
        random_string = random.choices(random_letters, k=length)
        password = "".join(random_string)
        result = f"""
Generated password
=================
 {password}
=================
{self.secure_password_detector(length)}"""
        return result
    
    def clear_terminal(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

if __name__ == '__main__':
    PasswordGenerator()