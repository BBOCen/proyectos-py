from persona import EmpleadoNormal, Directivo
from producto import Producto
from factura import Factura

producto1 = Producto("Portátil", 1000, "Dell")
producto2 = Producto("Ratón", 50, "Logitech")
producto3 = Producto("Teclado", 80, "Corsair")

empleado1 = EmpleadoNormal("Juan", 30)
directivo1 = Directivo("Ana", 40)

factura = Factura()
factura.agregar_producto(producto1)
factura.agregar_producto(producto2)
factura.agregar_producto(producto3)

factura.mostrar_factura()

print(f"\nEmpleado: {empleado1}")
print(f"Directivo: {directivo1}")
