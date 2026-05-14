number = int(input("Ingrese un numero: "))

if number % 2 == 0:
    print(f"{number} es un numero par")
else:
    print(f"{number} es un numero impar")


qualification = int(input("Ingrese una calificación: "))

if qualification >= 90:
    print(f"A")
elif qualification >= 80:
    print("B")
elif qualification >= 70:
    print("C")
else:
    print("D")

