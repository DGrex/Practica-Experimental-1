from typing import Any, List, Tuple, Dict, Set
from core import separator_decorator


class Variables:
    def __init__(self):
        self.chain: str = "Denis"
        self.list: List[int] = [1, 2, 3, 4, 5]
        self.dictionary: Dict[str, int] = {"Nombre": "Denis", "Edad": 5}

    def print_variables(self):        
        print(f"El primer carácter de {self.chain}: {self.chain[0]}")
        print(f"Ultimo elemento de {self.list}: {self.list[-1]}")
        print(f"Diccionario : {self.dictionary}")
        print(f"Valor de la clave 'Nombre': {self.dictionary["Nombre"]}")


@separator_decorator("Bloque 2 'Variables'")
def start_two():

    # Variables de todo tipo
    whole: int = 24
    floating: float = 23.9999
    chain: str = "Ana"
    boolean: bool = True
    null = None
    list: List[Any] = [1, "Gaby", True]
    tuple: Tuple = (6, "Hello", 3.79)
    dictionary: Dict[Any] = {"Name": "Gabriela", "Edad": 22}
    set: Set[int] = {1, 2, 3, 4}

    print("--Variables de cada tipo--")
    print(f" Entero: {whole}")
    print(f" Decimal: {floating}")
    print(f" Cadena: {chain}")
    print(f" Booleano: {boolean}")
    print(f" Nulo: {null}")
    print(f" Lista: {list}")
    print(f" Tupla: {tuple}")
    print(f" Diccionario: {dictionary}")
    print(f" Conjunto: {set}")

    # lista de 5 elementos
    list: List[int] = [1, 2, 3, 4, 5]
    print(f"\nLista de 5 elementos: {list}")
    print("Primer elemento",list[0])
    print("Ultimo elemento",list[-1])
    print("Elemento de posición 1 a 4",list[1:4])

    #instancia de la clase
    vrb = Variables()
    print()
    vrb.print_variables()
