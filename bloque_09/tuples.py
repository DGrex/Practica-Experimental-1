from typing import Tuple, Any

tuple: Tuple[Any] = ("Denis", "Javier", "Goyes", "Moran")

try:
    tuple[0] = "Elkin"
except TypeError as e:
    print("No es posible modificar una tupla\n",e)


numbers: Tuple[int] = (100,200,300,400)
a,b,*resto = numbers

print(a)
print(b)
print(resto)

