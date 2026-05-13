class Person:
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def print_person(self):
        return f"\nNombre: {self.name}\nEdad: {self.age}\n"

person_one = Person("Denis", 22)
person_two = Person("Monica", 44)
person_three = Person("Patricio", 20)

print(person_one.print_person())
print(person_two.print_person())
print(person_three.print_person())
