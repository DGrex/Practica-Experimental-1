from typing import Tuple

number: Tuple[int] = (10, 20, 30, 40)

first, *middle, last = number

print(f"Primera: {first}")
print(f"Mitad : {middle}")
print(f"Ultimo: {last}")

#
def multiply(a, b, c):
    return a * b * c


numbers = [2, 3, 4]

# Use * to unpack the list
result = multiply(*numbers)

print(result)  # 24

#
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

combined = {**dict1, **dict2}

print("dict1:", dict1)
print("dict2:", dict2)
print("combined:", combined)

