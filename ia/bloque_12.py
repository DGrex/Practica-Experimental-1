from typing import List, Any
from core import separator_decorator


@separator_decorator("Ejemplo IA Bloque 12")
def run_example():
    print("Este ejemplo demuestra manejo de excepciones comunes.")
    try:
        number = int(input("Ingrese un número: "))
        print(f"Número ingresado: {number}")
    except ValueError as error:
        print("Error: debe ingresar un número entero.")
        print(error)

    names: List[Any] = ["Denis", "Gabriela", "Ana"]
    try:
        print(names[5])
    except IndexError as error:
        print("Error: índice fuera de rango.")
        print(error)

    try:
        a = float(input("Ingrese el numerador: "))
        b = float(input("Ingrese el divisor: "))
        print(f"Resultado: {a / b}")
    except ValueError as error:
        print("Error: valor no válido.")
        print(error)
    except ZeroDivisionError as error:
        print("Error: división por cero.")
        print(error)
