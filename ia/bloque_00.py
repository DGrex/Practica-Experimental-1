from core import separator_decorator


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Nombre: {self.name}, Edad: {self.age}"


@separator_decorator("Ejemplo IA Bloque 0")
def run_example():
    print("Este ejemplo muestra cómo crear objetos y leer sus atributos.")
    person_one = Person("Ana", 21)
    person_two = Person("Luis", 30)
    print(person_one)
    print(person_two)
    print(
        "Se puede usar un método `__str__` para mostrar la información de forma clara."
    )
