class Factura:
    #La clase factura será una lista de todos los productos añadidos, con un método para calcular el valor de todos
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = sum([producto.precio for producto in self.productos])
        return total

    def mostrar_factura(self):
        for producto in self.productos:
            print(producto)
        print(f"Total: {self.calcular_total()}")
