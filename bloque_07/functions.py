def double(number):
    return number * 2

number: int = int(input("Ingrese un número:"))
print(double(number))


def addition(*numbers: int):
    return sum(numbers)

print(addition(2,3,4))


def factorial(number: int):
    if number == 0:
        return 1    
    return number * factorial(number-1)

print(factorial(5))