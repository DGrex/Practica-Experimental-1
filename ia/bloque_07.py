from core import separator_decorator


@separator_decorator("Ejemplo IA Bloque 7")
def run_example():
    print("Este ejemplo demuestra funciones simples y recursivas.")

    def double(value: int) -> int:
        return value * 2

    def addition(*values: int) -> int:
        return sum(values)

    def factorial(value: int) -> int:
        if value == 0:
            return 1
        return value * factorial(value - 1)

    value = int(input("Ingrese un número: "))
    print(f"Doble de {value}: {double(value)}")
    print(f"Suma ejemplo (2,3,4): {addition(2, 3, 4)}")
    print(f"Factorial de 5: {factorial(5)}")
