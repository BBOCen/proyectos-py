class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.libros = []
        self.prestamos = []

    #Funciones para agregar elementos

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    #Funciones para eliminar elementos

    def eliminar_usuario(self, indice):
        del self.usuarios[indice]

    def eliminar_prestamo(self, indice):
        del self.prestamos[indice]

    def eliminar_libros(self, indice):
        del self.libros[indice]

    #Funciones para imprimir todos los elementos

    def imprimir_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)

    def imprimir_prestamos(self):
        for prestamo in self.prestamos:
            print(prestamo)

    def imprimir_libros(self):
        for libro in self.libros:
            print(libro)
