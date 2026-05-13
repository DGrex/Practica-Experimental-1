class Product:

    def __init__(self, id: str, name: str, price: float):
        self.id = id
        self.name = name

        if price < 0:
            raise ValueError("El Precio no puede ser negativo")
        self.price = round(price,2)

    def print_product(self):
        return f"\nID: {self.id}\nProducto: {self.name}\nPrecio: {self.price}\n"

try:
    product_one = Product("P001", "Laptop", 662.257)
    print(product_one.print_product())
except ValueError as e:
    print(e)

try:
    product_two = Product("P002", "Teclado", -54.80)
    print(product_two.print_product())
except ValueError as e:
    print(e)

