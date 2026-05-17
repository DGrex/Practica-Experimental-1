from typing import Dict, Union
from core import separator_decorator


@separator_decorator("Ejemplo IA Bloque 10")
def run_example():
    print("Este ejemplo muestra operaciones con diccionarios.")
    person: Dict[str, Union[str, int]] = {
        "nombre": "Gabriela",
        "edad": 22,
        "ciudad": "Quito",
    }
    print(f"Nombre: {person['nombre']}")
    print(f"Edad: {person.get('edad')}")

    print("\nRecorrido de claves y valores:")
    for key, value in person.items():
        print(f"{key}: {value}")

    alias = person
    alias["apellido"] = "Caballero"
    print("\nDespués de modificar alias, el diccionario original cambia:")
    print(person)
