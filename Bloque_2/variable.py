from typing import Any, List, Tuple, Dict, Set

whole: int = 24
floating: float = 23.9999
chain: str = "Ana"
boolean: bool = True
null = None
list: List[Any] = [1, "Gaby", True]
tuple: Tuple = (6, "Hello", 3.79)
dictionary: Dict[Any] = {"Name": "Gabriela", "Edad": 22}
set: Set[int] = {1, 2, 3, 4}

print(f"\n Entero: {whole}")
print(f"\n Decimal: {floating}")
print(f"\n Cadena: {chain}")
print(f"\n Booleano: {boolean}")
print(f"\n Nulo: {null}")
print(f"\n Lista: {list}")
print(f"\n Tupla: {tuple}")
print(f"\n Diccionario: {dictionary}")
print(f"\n Conjunto: {set}")



list: List[int] = [1, 2, 3, 4, 5]
print(list[0])
print(list[-1])
print(list[1:4])
