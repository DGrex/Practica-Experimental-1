from typing import List, Any
from core import separator_decorator

@separator_decorator("Bloque 8 'Listas'")
def start_eight():
    print("--Ejercicio: Manejo de listas en Python--\n")

    # 1. Crear lista y agregar elementos
    names: List[str] = []
    names.append("Moran")
    names.append("Javier")
    names.append("Denis")
    names.sort()
    print("Lista ordenada de nombres:")
    print(f"Resultado: {names}")  # ['Denis', 'Javier', 'Moran']

    # 2. Operaciones con números
    numbers: List[int] = [5, 3, 8, 1, 9, 3]
    print("\nOperaciones con la lista de números:", numbers)
    print(f"Suma: sum({numbers}) = {sum(numbers)}")
    print(f"Máximo: max({numbers}) = {max(numbers)}")
    print(f"Mínimo: min({numbers}) = {min(numbers)}")

    # 3. Referencia vs copia
    num: List[int] = [1, 2, 3, 4, 5, 6]
    copy = num  # misma referencia
    copy.append(7)

    print("\nDemostración de referencia vs copia:")
    print(f"Lista original: {num}")
    print("Nota: al modificar 'copy', también cambia 'num' porque apuntan al mismo objeto.")

