from typing import Set, Any, List

set_one: Set[int] = {10, 11, 12, 13, 14}
set_two: Set[int] = {13, 14, 15, 16, 17}

print(set_one | set_two)
print(set_one & set_two)
print(set_one - set_two)
print(set_two - set_one)

numbers: set[int] = {1, 2, 2, 3, 3, 3, 4}
list_number: list[int] = list(numbers)

print(f"{list_number} esto es de tipo: {type(list_number)}")

1, 2, 3, 4
a: Set[int] = {1, 2, 3, 4}
b: Set[int] = {3, 4, 5, 6}

print(a | b)
print(a & b)
