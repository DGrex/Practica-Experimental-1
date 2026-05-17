from typing import Tuple, Any, List
from core import separator_decorator


@separator_decorator("Bloque 9 'Tuplas'")
def start_nine():
    print("--Ejercicio: Tuplas, inmutabilidad y desempaquetado--\n")

    # 1. Intentar modificar una tupla
    tuple_example: Tuple[Any] = ("Denis", "Javier", "Goyes", "Moran")
    try:
        tuple_example[0] = "Elkin"
    except TypeError as e:
        print("No es posible modificar una tupla (son inmutables).")
        print("Error generado:", e)

    # 2. Desempaquetado de tupla
    numbers: Tuple[int] = (100, 200, 300, 400)
    a, b, *rest = numbers
    print("\n--Desempaquetado de tupla--")
    print(f"Tupla original: {numbers}")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"resto = {rest}")

    # 3. Recorrer lista de coordenadas
    coordinates: List[Tuple[int, int]] = [(10, 7), (0, -5)]
    print("\n--Recorrido de coordenadas--")
    for x, y in coordinates:
        print(f"Coordenada en x: {x}, Coordenada en y: {y}")
