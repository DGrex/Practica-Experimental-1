from typing import Any, List
from core import separator_decorator

@separator_decorator("Bloque 6 'Bucles'")
def start_six():
    print("--Ejercicio: Bucles con while, for y list comprehension--\n")

    # 1. Números del 1 al 10 con while
    print("Números del 1 al 10 usando while:")
    number: int = 1
    while number <= 10:
        print(f"Iteración -> número actual: {number}")
        number += 1

    # 2. Recorrer lista de frutas con enumerate
    fruits: List[Any] = ["Manzana", "Uva", "Pera", "Frutilla"]
    print("\nLista de frutas con sus índices:")
    for index, fruit in enumerate(fruits):
        print(f"Índice {index} -> {fruit}")

    # 3. Lista de cuadrados de pares del 1 al 10 con list comprehension
    pair_squares: List[int] = [x**2 for x in range(1, 11) if x % 2 == 0]
    print("\nCuadrados de números pares del 1 al 10:")
    print(f"Expresión: [x**2 for x in range(1,11) if x % 2 == 0]")
    print(f"Resultado: {pair_squares}")
