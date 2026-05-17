from typing import Dict, Any
from core import separator_decorator


@separator_decorator("Bloque 5 'Condicionales'")
def start_five():
    print("--Ejercicio: Condicionales básicos--\n")

    # 1. Par o impar
    number = int(input("Ingrese un número: "))
    if number % 2 == 0:
        print(f"{number} es un número par (porque {number} % 2 = 0)")
    else:
        print(f"{number} es un número impar (porque {number} % 2 = 1)")

    # 2. Calificación con letras
    qualification = int(input("\nIngrese una calificación: "))
    print("--Resultado de la calificación--")
    if qualification >= 90:
        print(f"{qualification} -> A")
    elif qualification >= 80:
        print(f"{qualification} -> B")
    elif qualification >= 70:
        print(f"{qualification} -> C")
    else:
        print(f"{qualification} -> D")

    # 3. Sistema de login
    user: Dict[Any] = {"username": "admin", "password": "123"}
    username = input("\nIngrese su usuario: ")
    password = input("Ingrese su contraseña: ")

    print("--Resultado del login--")
    if username == user["username"] and password == user["password"]:
        print(f"Bienvenido {user['username']} (usuario y contraseña correctos)")
    else:
        print("Acceso Denegado (usuario o contraseña incorrectos)")
