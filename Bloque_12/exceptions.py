from typing import List, Any
from core import separator_decorator

@separator_decorator("Bloque 12 'Excepciones'")
def start_twelve():
    print("--Ejercicio: Manejo de excepciones en Python--\n")

    # 1. Captura de ValueError al convertir input
    try:
        number: int = int(input("Ingrese un número: "))
        print(f"El número ingresado es {number}")
    except ValueError as e:
        print("Error: el valor ingresado no es un número entero.")
        print("Detalle del error:", e)

    # 2. Captura de IndexError al acceder fuera de rango
    names: List[Any] = ["Denis", "Gabriela", "Ana"]
    try:
        print(f"Valor del 6to elemento: {names[5]}")
    except IndexError as e:
        print("Error: índice fuera de rango en la lista.")
        print("Detalle del error:", e)

    # 3. Captura de ValueError y ZeroDivisionError en división
    try:
        number_one: float = float(input("\nIngrese un número a dividir: "))
        number_two: float = float(input("Ingrese un número divisor: "))
        print(f"Operación: {number_one} / {number_two} = {number_one / number_two}")
    except ValueError as e:
        print("Error: debe ingresar un número válido.")
        print("Detalle del error:", e)
    except ZeroDivisionError as e:
        print("Error: no se puede dividir por cero.")
        print("Detalle del error:", e)
