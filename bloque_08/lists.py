from typing import List, Any

list: List[str] = []

list.append("Moran")
list.append("Javier")
list.append("Denis")
list.sort()
print(list) # Denis, Javier, Moran


numbers: int = [5, 3, 8, 1, 9, 3]

print(sum(numbers)) # 29
print(max(numbers)) #9
print(min(numbers)) #1

num: int = [1, 2, 3, 4, 5, 6]
copy = num
copy.append(7)

print(num)  # 1, 2, 3, 4, 5, 6, 7
