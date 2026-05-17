from typing import Any, Dict, List, Tuple, Set
from core import separator_decorator


@separator_decorator("Ejemplo IA Bloque 2")
def run_example():
    print("Este ejemplo muestra tipos de variables y cómo acceder a colecciones.")
    whole: int = 10
    floating: float = 3.14
    boolean: bool = True
    text: str = "Hola IA"
    data_list: List[Any] = [1, "dos", True]
    data_tuple: Tuple[int, str] = (5, "Cinco")
    data_dict: Dict[str, Any] = {"nombre": "Luis", "edad": 28}
    data_set: Set[int] = {1, 2, 3}

    print(f"Entero: {whole}")
    print(f"Decimal: {floating}")
    print(f"Booleano: {boolean}")
    print(f"Cadena: {text}")
    print(f"Lista: {data_list} -> primer elemento: {data_list[0]}")
    print(f"Tupla: {data_tuple} -> segundo elemento: {data_tuple[1]}")
    print(f"Diccionario: {data_dict} -> nombre: {data_dict['nombre']}")
    print(f"Conjunto: {data_set}")
