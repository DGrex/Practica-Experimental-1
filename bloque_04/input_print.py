from core import separator_decorator


@separator_decorator("Bloque 4 'Entrada y salida'")
def start_four():
    print("--Ejercicio: Entrada de datos y operaciones básicas--\n")

    # Primer ejercicio: nombre y edad
    name: str = input("Ingresar tu nombre: ")
    age: int = int(input("Ingrese su edad: "))
    print(f"Hola {name}, tu edad es {age} años.\n")

    # Segundo ejercicio: suma y promedio
    num_one: float = float(input("Ingrese el primer número: "))
    num_two: float = float(input("Ingrese el segundo número: "))

    addition: float = num_one + num_two
    average: float = addition / 2

    print("\n--Operaciones con números--")
    print(f"Suma: {num_one} + {num_two} = {addition}")
    print(f"Promedio: ({num_one} + {num_two}) / 2 = {average}.\n")

    # Tercer ejercicio: concatenación sin casting
    num_one: str = input("Ingrese el primer número (texto): ")
    num_two: str = input("Ingrese el segundo número (texto): ")

    print("\n--Concatenación de strings--")
    print(f"Suma (concatenación): {num_one} + {num_two} = {num_one + num_two}")
    print("Nota: aquí no se suman valores numéricos, se concatenan cadenas.")
