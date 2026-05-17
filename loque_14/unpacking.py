from typing import Tuple, List, Dict, Any
from core import separator_decorator

@separator_decorator("Bloque 14 'Unpacking'")
def start_fourteen():
    print("--Ejercicio: Desempaquetado de tuplas, listas y diccionarios--\n")

    # 1. Desempaquetado de tupla
    number: Tuple[int] = (10, 20, 30, 40)
    first, *middle, last = number
    print("Tupla original:", number)
    print(f"Primera: {first}")
    print(f"Mitad: {middle}")
    print(f"Último: {last}")

    # 2. Usar * para desempaquetar lista en función
    def multiply(a, b, c):
        return a * b * c

    numbers: List[int] = [2, 3, 4]
    result = multiply(*numbers)
    print("\n--Desempaquetado de lista en función--")
    print(f"Lista: {numbers}")
    print(f"Operación: {numbers[0]} * {numbers[1]} * {numbers[2]} = {result}")

    # 3. Combinar diccionarios con **
    dict1: Dict[str, Any] = {"a": 1, "b": 2}
    dict2: Dict[str, Any] = {"c": 3, "d": 4}
    combined: Dict[str, Any] = {**dict1, **dict2}

    print("\n--Combinación de diccionarios--")
    print("dict1:", dict1)
    print("dict2:", dict2)
    print("combined:", combined)

