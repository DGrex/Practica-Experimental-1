from core import separator_decorator


@separator_decorator("Ejemplo IA Bloque 4")
def run_example():
    print("Este ejemplo solicita datos al usuario y muestra operaciones básicas.")
    name: str = input("Ingrese su nombre: ")
    age: int = int(input("Ingrese su edad: "))
    print(f"Hola {name}, tienes {age} años.")

    num_one: float = float(input("Ingrese el primer número: "))
    num_two: float = float(input("Ingrese el segundo número: "))
    print(f"Suma: {num_one} + {num_two} = {num_one + num_two}")
    print(f"Promedio: {(num_one + num_two) / 2}")

    text_one: str = input("Ingrese un texto: ")
    text_two: str = input("Ingrese otro texto: ")
    print(f"Concatenación: {text_one + text_two}")
