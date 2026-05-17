from typing import List
from core import separator_decorator


@separator_decorator("Ejemplo IA Bloque 6")
def run_example():
    print("Este ejemplo muestra bucles `while`, `for` y listas por comprensión.")
    i = 1
    while i <= 5:
        print(f"While iteración: {i}")
        i += 1

    fruits: List[str] = ["Manzana", "Pera", "Uva"]
    for index, fruit in enumerate(fruits):
        print(f"Índice {index} -> {fruit}")

    squares: List[int] = [x**2 for x in range(1, 6) if x % 2 == 0]
    print(f"Cuadrados pares del 1 al 5: {squares}")
