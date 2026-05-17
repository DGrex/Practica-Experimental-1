import json
import re
from core import separator_decorator


@separator_decorator("Ejemplo IA Bloque 17")
def run_example():
    print("Este ejemplo usa mixins para promedio, validación y exportación.")

    class AverageMixin:
        def calculate_average(self, values: list[float]) -> float:
            if not values:
                return 0.0
            return sum(values) / len(values)

    class Student(AverageMixin):
        def __init__(self, name: str, grades: list[float]):
            self.name = name
            self.grades = grades

        def show_average(self):
            print(f"Promedio de {self.name}: {self.calculate_average(self.grades)}")

    student = Student("Maria", [8.0, 9.5, 10.0])
    student.show_average()

    class ValidationMixin:
        def validate_email(self, email: str) -> bool:
            pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            return re.match(pattern, email) is not None

    class User(ValidationMixin):
        def __init__(self, name: str, email: str, age: int):
            self.name = name
            self.email = email
            self.age = age

        def register(self):
            if not self.validate_email(self.email):
                print("Correo inválido")
                return
            if self.age < 18:
                print("Edad no permitida")
                return
            print(f"Usuario {self.name} registrado correctamente")

    user = User("Ana", "ana@gmail.com", 20)
    user.register()

    class ExportMixin:
        def export_json(self, data: list[dict]) -> str:
            return json.dumps(data, indent=2)

        def export_csv(self, data: list[dict]) -> str:
            if not data:
                return ""
            headers = data[0].keys()
            lines = [",".join(headers)]
            for row in data:
                lines.append(",".join(str(row[h]) for h in headers))
            return "\n".join(lines)

    class Report(ExportMixin):
        def __init__(self, data: list[dict]):
            self.data = data

        def show(self):
            print("JSON exportado:")
            print(self.export_json(self.data))
            print("CSV exportado:")
            print(self.export_csv(self.data))

    report = Report([{"producto": "Lapiz", "precio": 1.20}])
    report.show()
