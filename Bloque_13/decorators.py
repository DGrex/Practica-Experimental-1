from core import separator_decorator

class MyError(Exception):
    pass

@separator_decorator("Bloque 13 'Decoradores'")
def start_thirteen():
    print("--Ejercicio: Decoradores básicos y validaciones--\n")

    # 1. Decorador simple que imprime antes de ejecutar
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Iniciando...")
            result = func(*args, **kwargs)
            return result
        return wrapper

    @decorator
    def print_decorator():
        print("Se ejecutó la función")

    print("--Decorador simple--")
    print_decorator()

    # 2. Decorador que valida número positivo antes de calcular cuadrado
    def decorator_square(func):
        def wrapper(number):
            if not (number >= 0):
                raise MyError("Error: El número tiene que ser positivo")
            return func(number)
        return wrapper

    @decorator_square
    def square(number: float):
        return number**2

    print("\n--Decorador con validación--")
    try:
        number: float = float(input("Ingrese un número para calcular su cuadrado: "))
        print(f"Operación: {number} ** 2 = {round(square(number), 2)}")
    except ValueError as e:
        print("Error: ingresa un número válido.")
        print("Detalle:", e)
    except MyError as e:
        print("Error personalizado:", e)

    # 3. Decorador de log para mostrar ejecución de suma
    def log(func):
        def wrapper(a, b):
            print("Llamando a la función suma...")
            result = func(a, b)
            return result
        return wrapper

    @log
    def suma(a: float, b: float):
        return a + b

    number_one: float = 2
    number_two: float = 5
    print("\n--Decorador de log--")
    print(f"Operación: {number_one} + {number_two} = {suma(number_one, number_two)}")
