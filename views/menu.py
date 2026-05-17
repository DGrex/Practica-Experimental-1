from core import ConsoleUtils
from bloque_00.person import start
from bloque_01.product_student import start_two
import sys


class Menu:

    def __init__(self):
        pass

    def show_menu(self, title: str, options: list[dict], symbol: str = "="):
        while True:
            ConsoleUtils.clear_screen()
            ConsoleUtils.gotoxy(1, 1)
            ConsoleUtils.print_header(symbol * 40)
            ConsoleUtils.print_header(f" {title} ")
            ConsoleUtils.print_header(symbol * 40)
            for i, opt in enumerate(options, start=0):
                print(f"{i}. {opt['label']}")
            try:
                option = int(input("Ingrese una Opción: "))
                if 0 <= option < len(options):
                    action = options[option]["action"]
                    if action == "break":
                        break
                    elif action == "exit":
                        print("Cerrando el sistema...")
                        sys.exit()
                    elif callable(action):
                        action()
                        input("\nPresione Enter para continuar...")
                else:
                    print("Opción Incorrecta")
            except ValueError:
                print("Debe ingresar un número válido.")

    def optionMenu(self):
        self.show_menu(
            "Practica Experimental I",
            [
                {"label": "Ejercicios Bloque 0", "action": start},
                {"label": "Ejercicios Bloque 1", "action": start_two},
                {"label": "Salir", "action": "exit"},
            ],
        )


def safe_action(action, *args, **kwargs):
    try:
        return action(*args, **kwargs)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None
