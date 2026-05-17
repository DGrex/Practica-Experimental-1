import os

class ConsoleUtils:
    @staticmethod
    def clear_screen():
        """Clear the console screen."""
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def gotoxy(x, y):
        """Move cursor to position (x, y). 1-based."""
        print(f"\033[{y};{x}H", end="")
    
    @staticmethod
    def print_header(text):
        """Print a header with color."""
        print(f"\n{text}\n")