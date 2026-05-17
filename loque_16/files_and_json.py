import json
from core import separator_decorator

@separator_decorator("Bloque 16 'Archivos y JSON'")
def start_sixteen():
    print("--Ejercicio: Manejo de archivos de texto y JSON--\n")

    # 1. Escritura y lectura de archivo de texto
    with open("bloque_16/data/data_one.txt", "w") as f:
        f.write("Python\n")

    with open("bloque_16/data/data_one.txt", "r") as f:
        content = f.read()
        print("--Lectura de archivo de texto--")
        print("Contenido del archivo:")
        print(content)

    # 2. Guardar y cargar diccionario en JSON
    data = {"x": 10, "y": 25}
    with open("bloque_16/data/data_two.json", "w") as f:
        json.dump(data, f, indent=2)

    with open("bloque_16/data/data_two.json", "r") as f:
        charging = json.load(f)
        print("\n--Lectura de archivo JSON--")
        print(f"Valor de x: {charging['x']}")
        print(f"Valor de y: {charging['y']}")

    # 3. Guardar y recorrer lista de usuarios en JSON
    users = [
        {"nombre": "Gabriela", "apellido": "Caballero", "edad": 22},
        {"nombre": "Alex", "apellido": "Arboleda", "edad": 55}
    ]
    with open("bloque_16/data/users.json", "w") as f:
        json.dump(users, f)

    with open("bloque_16/data/users.json", "r") as f:
        loaded_users = json.load(f)
        print("\n--Lectura de lista de usuarios desde JSON--")
        for user in loaded_users:
            print(f"Nombre: {user['nombre']}")
            print(f"Apellido: {user['apellido']}")
            print(f"Edad: {user['edad']}\n")
