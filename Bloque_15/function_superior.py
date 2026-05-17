from functools import reduce
from core import separator_decorator

@separator_decorator("Bloque 15 'Funciones de orden superior'")
def start_fifteen():
    print("--Ejercicio: Uso de map, filter y reduce--\n")

    # 1. map() -> incrementar en 1 cada elemento
    list_one = [2, 4, 6]
    list_two = list(map(lambda x: x + 1, list_one))
    print("--map()--")
    print(f"Lista original: {list_one}")
    print(f"Operación: cada elemento + 1")
    print(f"Resultado: {list_two}")

    # 2. filter() -> obtener mayores a 3
    list_one = [1, 2, 3, 4, 5]
    list_two = list(filter(lambda x: x > 3, list_one))
    print("\n--filter()--")
    print(f"Lista original: {list_one}")
    print(f"Condición: elementos > 3")
    print(f"Resultado: {list_two}")

    # 3. reduce() -> multiplicar todos los elementos
    list_one = [1, 2, 3, 4]
    multiplication = reduce(lambda x, y: x * y, list_one)
    print("\n--reduce()--")
    print(f"Lista original: {list_one}")
    print("Operación: 1 * 2 * 3 * 4")
    print(f"Resultado: {multiplication}")
