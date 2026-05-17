import re

class ValidationMixin:
    def validate_email(self, email: str) -> bool:
        # Regex: al menos un texto antes del @, dominio y extensión
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
        

# Example
user1 = User("Luis", "luis@gmail.com", 20)
user1.register()   # Usuario Luis registrado correctamente.

user2 = User("Ana", "ana@correo", 15)
user2.register()   # Edad inválida, debe ser mayor o igual a 18.

user3 = User("Pedro", "pedro@@gmail", 25)
user3.register()   # Correo inválido.
