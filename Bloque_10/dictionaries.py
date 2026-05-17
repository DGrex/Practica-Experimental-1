from typing import Dict, Union
from core import separator_decorator

@separator_decorator("Bloque 10 'Diccionarios'")
def start_ten():
    print("--Ejercicio: Manejo de diccionarios en Python--\n")

    # 1. Crear diccionario de persona
    people: Dict[str, Union[str, int]] = {
        "nombre": "Gabriela",
        "edad": 22,
        "ciudad": "Babahoyo"
    }

    # Mostrar con claves
    print("Mostrar con claves:")
    print(f"Nombre: people['nombre'] -> {people['nombre']}")
    print(f"Edad: people.get('edad') -> {people.get('edad', 'La clave no existe')}")

    # Mostrar con items
    print("\nMostrar con items:")
    for key, value in people.items():
        print(f"{key}: {value}")

    # Agregado por referencia
    print("\nAgregado por referencia:")
    copy = people  # misma referencia
    copy["Apellido"] = "Caballero"

    print("Diccionario original modificado (porque copy apunta al mismo objeto):")
    print(people)
