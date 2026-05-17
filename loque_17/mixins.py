import re
import json
from core import separator_decorator

@separator_decorator("Bloque 17 'Mixins'")
def start_seventeen():
    print("--Ejercicio: Uso de Mixins para reutilizar funcionalidades--\n")

    # 1. Promedio con AverageMixin
    class AverageMixin:
        def calculate_average(self, grades: list[float]) -> float:
            if not grades:
                return 0.0
            return sum(grades) / len(grades)

    class Student(AverageMixin):
        def __init__(self, name: str, grades: list[float]):
            self.name = name
            self.grades = grades

        def show_average(self):
            average = self.calculate_average(self.grades)
            print(f"El promedio de {self.name} es {average}")

    print("--AverageMixin--")
    student = Student("Gabriela", [8, 9, 10])
    student.show_average()   # El promedio de Gabriela es 9.0

    # 2. Validación con ValidationMixin
    class ValidationMixin:
        def validate_email(self, email: str) -> bool:
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            return re.match(pattern, email) is not None

    class User(ValidationMixin):
        def __init__(self, name: str, email: str, age: int):
            self.name = name
            self.email = email
            self.age = age

        def register(self):
            if not self.validate_email(self.email):
                print("Correo inválido.")
                return
            if self.age < 18:
                print("Edad inválida, debe ser mayor o igual a 18.")
                return
            print(f"Usuario {self.name} registrado correctamente.")

    print("\n--ValidationMixin--")
    user1 = User("Luis", "luis@gmail.com", 20)
    user1.register()
    user2 = User("Ana", "ana@correo", 15)
    user2.register()
    user3 = User("Pedro", "pedro@@gmail", 25)
    user3.register()

    # 3. Exportación con ExportMixin
    class ExportMixin:
        def export_json(self, data: list[dict]) -> str:
            return json.dumps(data, indent=4)

        def export_csv(self, data: list[dict]) -> str:
            if not data:
                return ""
            headers = data[0].keys()
            lines = [",".join(headers)]
            for d in data:
                lines.append(",".join(str(d[h]) for h in headers))
            return "\n".join(lines)

    class Report(ExportMixin):
        def __init__(self, data: list[dict]):
            self.data = data

        def show_exports(self):
            print("\n--ExportMixin--")
            print("JSON:")
            print(self.export_json(self.data))
            print("\nCSV:")
            print(self.export_csv(self.data))

    sales = [
        {"producto": "Laptop", "precio": 1200},
        {"producto": "Mouse", "precio": 25}
    ]
    report = Report(sales)
    report.show_exports()
