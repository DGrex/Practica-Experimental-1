
from typing import Tuple

number : Tuple[int] =  (10, 20, 30, 40)

first, *middle, last = number

print(f"Primera: {first}")
print(f"Mitad : {middle}")
print(f"Ultimo: {last}")