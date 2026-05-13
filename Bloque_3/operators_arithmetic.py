a: float = 20
b: float = 4

print(f"Resultado de suma: {a+b}")
print(f"Resultado de resta: {a-b}")
print(f"Resultado de multiplicación: {a*b}")
print(f"Resultado de división decimal: {a/b}")
print(f"Resultado de división entera: {a//b}")
print(f"Resultado de modulo: {a%b}")
print(f"Resultado de potencia: {a**b}")

from typing import List, Any

list_one: List[int] = [1, 2, 3, 4, 5]
list_two: List[Any] = [1, 2, 3, 4, 5]
print(f"Demostración con == :{list_one == list_two}")
print(f"Demostración con is :{list_one is list_two}")


x = 2 + 1 * 2 % 2 + (2**1)//2
print(x)
"""
Orden De resolución
1. El paréntesis y la potencia
2. La multiplicación
3. El modulo
4. La división entera
5. Las sumas 
"""