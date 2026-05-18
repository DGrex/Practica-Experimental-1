from core import ConsoleUtils
import sys
from ia.bloque_00 import run_example as example_0
from ia.bloque_01 import run_example as example_1
from ia.bloque_02 import run_example as example_2
from ia.bloque_03 import run_example as example_3
from ia.bloque_04 import run_example as example_4
from ia.bloque_05 import run_example as example_5
from ia.bloque_06 import run_example as example_6
from ia.bloque_07 import run_example as example_7
from ia.bloque_08 import run_example as example_8
from ia.bloque_09 import run_example as example_9
from ia.bloque_10 import run_example as example_10
from ia.bloque_11 import run_example as example_11
from ia.bloque_12 import run_example as example_12
from ia.bloque_13 import run_example as example_13
from ia.bloque_14 import run_example as example_14
from ia.bloque_15 import run_example as example_15
from ia.bloque_16 import run_example as example_16
from ia.bloque_17 import run_example as example_17


class IAExamplesMenu:

    def __init__(self):
        pass

    def show_menu(self, title: str, options: list[dict], symbol: str = "="):
        while True:
            ConsoleUtils.clear_screen()

            # Prepare menu lines
            menu_lines = []
            for i, opt in enumerate(options, start=0):
                menu_lines.append(f"{i}. {opt['label']}")

            # Print the box with menu
            ConsoleUtils.print_box(title, menu_lines)

            try:
                option = int(input("\nIngrese una opción: "))
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
                    print("Opción incorrecta")
            except ValueError:
                print("Debe ingresar un número válido.")

    def optionMenu(self):
        self.show_menu(
            "Ejemplos IA por Bloque",
            [
                {"label": "Bloque 0 - IA: objetos Person", "action": example_0},
                {"label": "Bloque 1 - IA: Product y Student", "action": example_1},
                {
                    "label": "Bloque 2 - IA: Variables y colecciones",
                    "action": example_2,
                },
                {
                    "label": "Bloque 3 - IA: Operadores y precedencia",
                    "action": example_3,
                },
                {"label": "Bloque 4 - IA: Input y print", "action": example_4},
                {"label": "Bloque 5 - IA: Condicionales y login", "action": example_5},
                {"label": "Bloque 6 - IA: Bucles y comprehension", "action": example_6},
                {"label": "Bloque 7 - IA: Funciones y recursión", "action": example_7},
                {"label": "Bloque 8 - IA: Listas", "action": example_8},
                {"label": "Bloque 9 - IA: Tuplas", "action": example_9},
                {"label": "Bloque 10 - IA: Diccionarios", "action": example_10},
                {"label": "Bloque 11 - IA: Conjuntos", "action": example_11},
                {"label": "Bloque 12 - IA: Excepciones", "action": example_12},
                {"label": "Bloque 13 - IA: Decoradores", "action": example_13},
                {"label": "Bloque 14 - IA: Unpacking", "action": example_14},
                {
                    "label": "Bloque 15 - IA: Funciones de orden superior",
                    "action": example_15,
                },
                {"label": "Bloque 16 - IA: Archivos y JSON", "action": example_16},
                {"label": "Bloque 17 - IA: Mixins", "action": example_17},
                {"label": "Volver al menú principal", "action": "break"},
            ],
        )
