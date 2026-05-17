from typing import List, Any
from core import separator_decorator


@separator_decorator("Ejemplo IA Bloque 3")
def run_example():
    print("Este ejemplo muestra operadores aritméticos y la comunicación entre listas.")
    a: float = 12
    b: float = 5
    print(f"Suma: {a} + {b} = {a + b}")
    print(f"Resta: {a} - {b} = {a - b}")
    print(f"Multiplicación: {a} * {b} = {a * b}")
    print(f"División: {a} / {b} = {a / b}")
    print(f"Potencia: {a} ** {b} = {a ** b}")

    list_one: List[int] = [1, 2, 3]
    list_two: List[Any] = [1, 2, 3]
    print(f"list_one == list_two -> {list_one == list_two}")
    print(f"list_one is list_two -> {list_one is list_two}")
    x = 2 + 1 * 2 % 2 + (2**1) // 2
    print(f"Precedencia: 2 + 1 * 2 % 2 + (2**1)//2 = {x}")
