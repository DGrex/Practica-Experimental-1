from core import separator_decorator

@separator_decorator("Bloque 7 'Funciones'")
def start_seven():
    print("--Ejercicio: Funciones básicas, *args y recursividad--\n")

    # 1. Función que calcula el doble
    def double(number: int) -> int:
        return number * 2

    number: int = int(input("Ingrese un número: "))
    print(f"Operación: {number} * 2 = {double(number)}")

    # 2. Función que suma todos los elementos con *args
    def addition(*numbers: int) -> int:
        return sum(numbers)

    print("\n--Suma con *args--")
    print(f"Operación: 2 + 3 + 4 = {addition(2,3,4)}")

    # 3. Función recursiva para calcular factorial
    def factorial(number: int) -> int:
        if number == 0:
            return 1
        return number * factorial(number-1)

    print("\n--Factorial con recursividad--")
    print("Operación: factorial(5) = 5 * 4 * 3 * 2 * 1")
    print(f"Resultado: {factorial(5)}")
