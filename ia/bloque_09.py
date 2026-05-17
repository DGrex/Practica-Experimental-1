from typing import Tuple, Any, List
from core import separator_decorator


@separator_decorator("Ejemplo IA Bloque 9")
def run_example():
    print("Este ejemplo demuestra tuplas inmutables y desempaquetado.")
    data: Tuple[Any, ...] = ("Denis", "Javier", "Goyes", "Moran")
    try:
        data[0] = "Pablo"
    except TypeError as error:
        print("Error: no se puede modificar una tupla.")
        print(error)

    a, b, *rest = data
    print(f"Primer elemento: {a}")
    print(f"Segundo elemento: {b}")
    print(f"Resto: {rest}")

    coordinates: List[Tuple[int, int]] = [(10, 7), (0, -5)]
    for x, y in coordinates:
        print(f"Coordenada: x={x}, y={y}")
