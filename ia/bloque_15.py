from functools import reduce
from core import separator_decorator


@separator_decorator("Ejemplo IA Bloque 15")
def run_example():
    print("Este ejemplo demuestra map, filter y reduce.")

    numbers = [1, 2, 3, 4, 5]
    plus_one = list(map(lambda x: x + 1, numbers))
    print(f"map: {numbers} -> {plus_one}")

    filtered = list(filter(lambda x: x > 3, numbers))
    print(f"filter: elementos mayores a 3 -> {filtered}")

    product = reduce(lambda x, y: x * y, numbers)
    print(f"reduce: multiplicación total -> {product}")
