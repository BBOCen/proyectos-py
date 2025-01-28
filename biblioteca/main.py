from usuario import Usuario
from libro import Libro
from biblioteca import Biblioteca
from prestamo import Prestamo

usuario1 = Usuario("Juan Perez", "U001")
usuario2 = Usuario("Maria Lopez", "U002")

libro1 = Libro("El Quijote", "Miguel de Cervantes", 1605, False)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, True)

biblioteca = Biblioteca()

biblioteca.agregar_usuario(usuario1)
biblioteca.agregar_usuario(usuario2)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

prestamo1 = Prestamo(libro2, usuario1)
biblioteca.agregar_prestamo(prestamo1)

print("Usuarios en la biblioteca:")
biblioteca.imprimir_usuarios()
print("\n")

print("Libros en la biblioteca:")
biblioteca.imprimir_libros()
print("\n")

print("Préstamos en la biblioteca:")
biblioteca.imprimir_prestamos()
print("\n")

biblioteca.eliminar_usuario(1)
biblioteca.eliminar_libros(0)

print("Usuarios restantes en la biblioteca:")
biblioteca.imprimir_usuarios()
print("\n")

print("Libros restantes en la biblioteca:")
biblioteca.imprimir_libros()
print("\n")

print("Préstamos restantes en la biblioteca:")
biblioteca.imprimir_prestamos()