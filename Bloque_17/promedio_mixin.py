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
        


student = Student("Gabriela", [8, 9, 10])
student.show_average()   # El promedio de Gabriela es 9.0
