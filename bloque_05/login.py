from typing import Dict, Any

user: Dict[Any] = {"username": "admin", "password": "123"}

username = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

if username == user["username"] and password == user["password"]:
    print(f"Bienvenido {user["username"]}")
else:
    print("Acceso Denegado")