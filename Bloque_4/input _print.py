name :str = input("Ingresar tu nombre: ")
age :int = int(input("Ingrese su edad: "))

print(f"Hola {name} tu edad es {age} años")


num_one: float = float(input("Ingrese el primer numero: "))
num_two: float = float(input("Ingrese el segundo numero: "))

addition: float = num_one + num_two
average: float = addition / 2

print("Suma", addition, sep=": ")
print(f"Promedio: {average}", end=".\n")


num_one: float = input("Ingrese el primer numero: ")
num_two: float = input("Ingrese el segundo numero: ")

print(f"Suma: {num_one+num_two}") #Imprime los números concatenados