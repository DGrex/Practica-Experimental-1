from typing import Set, List
from core import separator_decorator


@separator_decorator("Ejemplo IA Bloque 11")
def run_example():
    print("Este ejemplo muestra operaciones con conjuntos.")
    a: Set[int] = {1, 2, 3}
    b: Set[int] = {3, 4, 5}
    print(f"A = {a}")
    print(f"B = {b}")
    print(f"Unión: {a | b}")
    print(f"Intersección: {a & b}")
    print(f"Diferencia A - B: {a - b}")
    print(f"Diferencia B - A: {b - a}")

    numbers: Set[int] = {1, 2, 2, 3, 3, 4}
    print(f"Conjunto sin duplicados: {numbers}")
    print(f"Convertido a lista: {list(numbers)}")
