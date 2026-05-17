from core import separator_decorator
from typing import Dict, List

class Product:

    def __init__(self, id: str, name: str, price: float):
        self.id = id
        self.name = name

        if price < 0:
            raise ValueError("El Precio no puede ser negativo")
        self.price = round(price,2)

    def print_product(self):
        return f"\nID: {self.id}\nProducto: {self.name}\nPrecio: {self.price}\n"
   

class Student:
    def __init__(self, name: str, qualifications: List = None):
        self.name = name

        if qualifications is None:
            self.qualifications = []
        else:
            self.qualifications = qualifications

    def print_student(self):
        return f"\nNombre: {self.name}\nNotas: {self.qualifications}\n"

    @classmethod
    def from_dictionary(cls, data: Dict[str, object]):
        return cls(data["name"], data["qualifications"])




@separator_decorator("Ejercicios Bloque 1")
def start_two():
    print("\n--Instancias de Productos--")
    try:
        product_one = Product("P001", "Laptop", 662.257)
        print(product_one.print_product())
    except ValueError as e:
        print(e)

    print("--Instancia con un valor negativo--")
    try:
        product_two = Product("P002", "Teclado", -54.80)
        print(product_two.print_product())
    except ValueError as e:
        print(e)
    
    print("\n--Objeto creado desde 'from_dictionary'--")
    data = {"name": "Denis", "qualifications": [10, 7]}
    student = Student.from_dictionary(data)
    print(student.print_student())