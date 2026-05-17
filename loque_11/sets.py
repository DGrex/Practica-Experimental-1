from typing import Set, Any, List
from core import separator_decorator

@separator_decorator("Bloque 11 'Conjuntos'")
def start_eleven():
    print("--Ejercicio: Operaciones con conjuntos en Python--\n")

    # 1. Operaciones básicas entre dos conjuntos
    set_one: Set[int] = {10, 11, 12, 13, 14}
    set_two: Set[int] = {13, 14, 15, 16, 17}

    print("Conjunto 1:", set_one)
    print("Conjunto 2:", set_two)
    print("\nOperaciones:")
    print(f"Unión: {set_one} | {set_two} = {set_one | set_two}")
    print(f"Intersección: {set_one} & {set_two} = {set_one & set_two}")
    print(f"Diferencia: {set_one} - {set_two} = {set_one - set_two}")
    print(f"Diferencia inversa: {set_two} - {set_one} = {set_two - set_one}")

    # 2. Eliminar duplicados de una lista usando set
    numbers: Set[int] = {1, 2, 2, 3, 3, 3, 4}
    list_number: List[int] = list(numbers)
    print("\nEliminar duplicados de una lista:")
    print(f"Lista original con repetidos: [1, 2, 2, 3, 3, 3, 4]")
    print(f"Lista sin duplicados: {list_number} -> tipo: {type(list_number)}")

    # 3. Más operaciones con conjuntos
    a: Set[int] = {1, 2, 3, 4}
    b: Set[int] = {3, 4, 5, 6}
    print("\nConjunto A:", a)
    print("Conjunto B:", b)
    print(f"Unión: A | B = {a | b}")
    print(f"Intersección: A & B = {a & b}")
