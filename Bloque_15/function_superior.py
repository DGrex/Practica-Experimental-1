from functools import reduce

list_one = [2, 4, 6]
list_two = list(map(lambda x: x + 1, list_one))

print("Lista original: ", list_one)
print("Lista mas uno: ", list_two)

list_one = [1, 2, 3, 4, 5]

list_two = list(filter(lambda x: x > 3, list_one))
print(f"Lista original: {list_one}")
print(f"Mayores a 3 de la lista: {list_two}")

list_one = [1, 2, 3, 4]
multiplication = reduce(lambda x,y: x*y, list_one)
print(f"Lista : {list_one}")
print(f"Multiplicación de toda la lista: {multiplication}")

