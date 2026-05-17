with open("bloque_16/data/data_one.txt", "w") as f:
    f.write("Python\n")
 
with open("bloque_16/data/data_one.txt", "r") as f:
    content = f.read()
    print(content)
    
import json

data = {"x": 10, "y": 25}
with open("bloque_16/data/data_two.json", "w") as f:
    json.dump(data, f, indent=2)


with open("bloque_16/data/data_two.json", "r") as f:
    charging = json.load(f)
    print("Valor de x", charging["x"]) 
    print("Valor de y", charging["y"]) 


user = [
 {"nombre": "Gabriela","apellido": "Caballero", "edad": 22},
 {"nombre": "Alex","apellido": "Arboleda", "edad": 55}
 ]
with open("bloque_16/data/users.json", "w") as f:
    json.dump(user, f)

with open("bloque_16/data/users.json","r") as f:
    loaded_users = json.load(f)
    for user in loaded_users:
        print(f"\nNombre: {user["nombre"]}\nApellido: {user["apellido"]}\nEdad: {user["edad"]}\n")

