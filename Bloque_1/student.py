from typing import Dict, List

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


data = {"name": "Denis", "qualifications": [10, 7]}
student = Student.from_dictionary(data)

print(student.print_student())
