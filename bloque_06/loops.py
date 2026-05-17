number: int = 1

while number <= 10:
    print(number)
    number += 1


from typing import Any, List

fruits: List[Any] = ["Manzana", "Uva", "Pera", "Frutilla"]

for value, fruit in enumerate(fruits):
    print(f"{value} -> {fruit}")

pair_squares: List[int] = [x**2 for x in range(1,11) if x % 2 == 0]
print(pair_squares)
