from typing import List, Any
from core import separator_decorator


@separator_decorator("Ejemplo IA Bloque 8")
def run_example():
    print("Este ejemplo usa listas: agregar, ordenar, sumar y copiar.")
    names: List[str] = ["Moran", "Javier", "Denis"]
    names.sort()
    print(f"Lista ordenada: {names}")

    numbers: List[int] = [5, 2, 8, 1]
    print(f"Sumatoria: {sum(numbers)}")
    print(f"Mayor: {max(numbers)}")
    print(f"Menor: {min(numbers)}")

    numbers_copy = numbers
    numbers_copy.append(10)
    print(f"Misma referencia agrega 10: {numbers}")
    print("Nota: `numbers_copy` y `numbers` apuntan al mismo objeto.")
