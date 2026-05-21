import csv
import json
import re
from io import StringIO
from pathlib import Path
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
            return json.dumps(data, indent=2, ensure_ascii=False)

        def export_csv(self, data: list[dict]) -> str:
            if not data:
                return ""
            headers = list(data[0].keys())
            output = StringIO()
            writer = csv.DictWriter(output, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
            return output.getvalue()

        def save_json_file(self, data: list[dict], file_path: Path | str) -> None:
            path = Path(file_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=2, ensure_ascii=False)

        def save_csv_file(self, data: list[dict], file_path: Path | str) -> None:
            path = Path(file_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=list(data[0].keys()))
                writer.writeheader()
                writer.writerows(data)

    class Report(ExportMixin):
        def __init__(self, data: list[dict]):
            self.data = data

        def show(self):
            print("JSON exportado:")
            print(self.export_json(self.data))
            print("CSV exportado:")
            print(self.export_csv(self.data))

            output_folder = Path("ia/data")
            self.save_json_file(self.data, output_folder / "ia_report.json")
            self.save_csv_file(self.data, output_folder / "ia_report.csv")
            print(f"\nArchivos guardados en: {output_folder.resolve()}")

    report = Report([{"producto": "Lapiz", "precio": 1.20}])
    report.show()
