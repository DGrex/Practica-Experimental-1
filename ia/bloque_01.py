from core import separator_decorator
from typing import Dict, List


class Product:
    def __init__(self, id: str, name: str, price: float):
        if price < 0:
            raise ValueError("El precio no puede ser negativo")
        self.id = id
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"ID: {self.id} - Producto: {self.name} - Precio: {self.price}"


class Student:
    def __init__(self, name: str, qualifications: List[int]):
        self.name = name
        self.qualifications = qualifications

    def __str__(self) -> str:
        return f"{self.name} - Notas: {self.qualifications}"

    @classmethod
    def from_dict(cls, data: Dict[str, object]):
        return cls(data["name"], data["qualifications"])


@separator_decorator("Ejemplo IA Bloque 1")
def run_example():
    print("Este ejemplo crea un producto y un estudiante, con validación de datos.")
    try:
        product = Product("PR01", "Auriculares", 45.50)
        print(product)
    except ValueError as error:
        print(error)

    data = {"name": "María", "qualifications": [9, 8, 10]}
    student = Student.from_dict(data)
    print(student)
