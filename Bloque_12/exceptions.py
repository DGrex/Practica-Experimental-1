from typing import List, Any

try:
    number: int = int(input("Ingrese un numero: "))
    print(f"El numero es {number}")
except ValueError as e:
    print(e)


list: List[Any] = ["Denis","Gabriela","Ana"] 

try:
       print(f"Valor del 6 item: {list[5]}")
except IndexError as e:
    print(e)
    
try:
    number_one: float = float(input("Ingrese un numero a dividir: "))
    number_two: float = float(input("Ingrese un numero divisor: "))
    print(f"Resultado de la división = {number_one / number_two}")
except ValueError as e:
    print(e)
except ZeroDivisionError as e :
    print(e)