from typing import Dict, Union

people: Dict[str, Union[str, int]] = {"nombre":"Gabriela", "edad": 22, "ciudad":"Babahoyo"}

print("Mostrar con Claves")
print("Nombre: ",people["nombre"])
print("Edad: ",people.get("edad", "La clave no existe"))

print("\nMostrar con items")
for key, value in people.items():
    print(f"{key}: {value}")
    
print("\nAgregado Por referencia")
copy = people
copy["Apellido"] = "Caballero"

print(people)