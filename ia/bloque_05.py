from core import separator_decorator


@separator_decorator("Ejemplo IA Bloque 5")
def run_example():
    print("Este ejemplo aplica condicionales para par/impar, calificaciones y login.")
    number: int = int(input("Ingrese un número: "))
    if number % 2 == 0:
        print(f"{number} es par.")
    else:
        print(f"{number} es impar.")

    grade: int = int(input("Ingrese una calificación (0-100): "))
    if grade >= 90:
        print("Calificación: A")
    elif grade >= 80:
        print("Calificación: B")
    elif grade >= 70:
        print("Calificación: C")
    else:
        print("Calificación: D")

    print("\nEjemplo de login:")
    user = {"username": "admin", "password": "123"}
    username = input("Usuario: ")
    password = input("Contraseña: ")
    if username == user["username"] and password == user["password"]:
        print("Acceso concedido.")
    else:
        print("Acceso denegado.")
