class Producto:
    def __init__(self, nombre, precio, marca):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Marca: {self.marca}"
