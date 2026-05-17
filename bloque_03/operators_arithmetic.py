from typing import List, Any
from core import separator_decorator


@separator_decorator("Bloque 3 'Operadores'")
def start_three():
    print("--Ejercicio: Operadores aritméticos y comparaciones--\n")

    a: float = 20
    b: float = 4

    # Operadores aritméticos mostrando la operación
    print(f"Suma: {a} + {b} = {a+b}")
    print(f"Resta: {a} - {b} = {a-b}")
    print(f"Multiplicación: {a} * {b} = {a*b}")
    print(f"División decimal: {a} / {b} = {a/b}")
    print(f"División entera: {a} // {b} = {a//b}")
    print(f"Módulo: {a} % {b} = {a%b}")
    print(f"Potencia: {a} ** {b} = {a**b}")

    # Comparación de listas
    list_one: List[int] = [1, 2, 3, 4, 5]
    list_two: List[Any] = [1, 2, 3, 4, 5]
    print("\n--Comparaciones con == y is--")
    print(f"list_one == list_two -> {list_one == list_two}")
    print(f"list_one is list_two -> {list_one is list_two}")

    # Precedencia de operadores
    x = 2 + 1 * 2 % 2 + (2**1) // 2
    print("\n--Ejercicio de precedencia--")
    print(f"Expresión: 2 + 1 * 2 % 2 + (2**1)//2")
    print(f"Resultado: {x}")
    print("""
Orden de resolución:
1. El paréntesis y la potencia
2. La multiplicación
3. El módulo
4. La división entera
5. Las sumas
""")
