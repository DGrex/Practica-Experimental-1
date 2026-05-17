from core import separator_decorator


@separator_decorator("Ejemplo IA Bloque 13")
def run_example():
    print("Este ejemplo muestra decoradores simples.")

    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Antes de la función")
            return func(*args, **kwargs)

        return wrapper

    @decorator
    def greet(name: str):
        print(f"Hola {name}")

    greet("Mundo")

    def positive_only(func):
        def wrapper(value: float):
            if value < 0:
                raise ValueError("Solo se aceptan números positivos")
            return func(value)

        return wrapper

    @positive_only
    def square(value: float) -> float:
        return value**2

    value = float(input("Ingrese un número positivo para elevar al cuadrado: "))
    try:
        print(f"Resultado: {square(value)}")
    except ValueError as error:
        print(error)
