from core import ConsoleUtils
from bloque_00.person import start
from bloque_01.product_student import start_one
from bloque_02.variable import start_two
from bloque_03.operators_arithmetic import start_three
from bloque_04.input_print import start_four
from bloque_05.conditionals import start_five
from bloque_06.loops import start_six
from bloque_07.functions import start_seven
from bloque_08.lists import start_eight
from bloque_09.tuples import start_nine
from bloque_10.dictionaries import start_ten
from bloque_11.sets import start_eleven
from bloque_12.exceptions import start_twelve
from bloque_13.decorators import start_thirteen
from bloque_14.unpacking import start_fourteen
from bloque_15.function_superior import start_fifteen
from bloque_16.files_and_json import start_sixteen
from bloque_17.mixins import start_seventeen
from .menu_ia import IAExamplesMenu
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
            for i, opt in enumerate(options, start=1):
                print(f"{i}. {opt['label']}")
            try:
                option = int(input("Ingrese una Opción: "))
                if 1 <= option <= len(options):
                    action = options[option - 1]["action"]
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
                {"label": "Ejercicios Bloque 0 (Intro)", "action": start},
                {"label": "Ejercicios Bloque 1 (Variables)", "action": start_one},
                {
                    "label": "Ejercicios Bloque 2 (Condiciones básicas)",
                    "action": start_two,
                },
                {"label": "Ejercicios Bloque 3 (Operadores)", "action": start_three},
                {"label": "Ejercicios Bloque 4 (Entrada/Salida)", "action": start_four},
                {"label": "Ejercicios Bloque 5 (Condicionales)", "action": start_five},
                {"label": "Ejercicios Bloque 6 (Bucles)", "action": start_six},
                {"label": "Ejercicios Bloque 7 (Funciones)", "action": start_seven},
                {"label": "Ejercicios Bloque 8 (Listas)", "action": start_eight},
                {"label": "Ejercicios Bloque 9 (Tuplas)", "action": start_nine},
                {"label": "Ejercicios Bloque 10 (Diccionarios)", "action": start_ten},
                {"label": "Ejercicios Bloque 11 (Conjuntos)", "action": start_eleven},
                {"label": "Ejercicios Bloque 12 (Excepciones)", "action": start_twelve},
                {
                    "label": "Ejercicios Bloque 13 (Decoradores)",
                    "action": start_thirteen,
                },
                {"label": "Ejercicios Bloque 14 (Unpacking)", "action": start_fourteen},
                {
                    "label": "Ejercicios Bloque 15 (Funciones de orden superior)",
                    "action": start_fifteen,
                },
                {
                    "label": "Ejercicios Bloque 16 (Archivos y JSON)",
                    "action": start_sixteen,
                },
                {"label": "Ejercicios Bloque 17 (Mixins)", "action": start_seventeen},
                {"label": "Ejemplos_IA", "action": self.show_ia_examples},
                {"label": "Salir", "action": "exit"},
            ],
        )

    def show_ia_examples(self):
        IAExamplesMenu().optionMenu()


def safe_action(action, *args, **kwargs):
    try:
        return action(*args, **kwargs)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None
