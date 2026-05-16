class MyError(Exception):
    pass


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Iniciando...")
        result = func(*args, **kwargs)

        return result

    return wrapper


@decorator
def print_decorator():
    print("Se ejecuto la función")


# print_decorator()


def decorator_square(func):
    def wrapper(number):
        if not (number >= 0):
            raise MyError("Error: El numero tiene que ser positivo")
            return None
        return func(number)

    return wrapper


@decorator_square
def square(number: float):
    return number**2


try:
    number: float = float(input("Cuadrado del numero: "))
    print("es: ", round(square(number), 2))
except ValueError as e:
    print(e)
    print("Ingresa un numero valido")
except MyError as e:
    print(e)


def log(func):
    def wrapper(a, b):
        print("Llamando a la función")
        result = func(a, b)
        return result

    return wrapper


@log
def suma(a: float, b: float):
    return a + b


number_one: float = 2
number_two: float = 5

print(f"{number_one} + {number_two} = {suma(number_one,  number_two)}")
