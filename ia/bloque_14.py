from typing import Tuple, List, Dict, Any
from core import separator_decorator


@separator_decorator("Ejemplo IA Bloque 14")
def run_example():
    print("Este ejemplo muestra desempaquetado y combinación de colecciones.")

    numbers: Tuple[int, ...] = (10, 20, 30, 40)
    first, *middle, last = numbers
    print(f"Tupla original: {numbers}")
    print(f"Primero: {first}, Medio: {middle}, Último: {last}")

    def multiply(a: int, b: int, c: int) -> int:
        return a * b * c

    values: List[int] = [2, 3, 4]
    print(f"Multiplicación desempaquetada: {multiply(*values)}")

    dict1: Dict[str, Any] = {"a": 1, "b": 2}
    dict2: Dict[str, Any] = {"c": 3, "d": 4}
    combined: Dict[str, Any] = {**dict1, **dict2}
    print(f"Diccionarios combinados: {combined}")
