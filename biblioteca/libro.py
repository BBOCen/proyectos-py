class Libro:
    def __init__(self, nombre, autor, anio, prestado):
        self.nombre = nombre
        self.autor = autor
        self.anio = anio
        self.prestado = prestado

    def __str__(self):
        return f"Productos: \nNombre: {self.nombre} \nAutor: {self.autor} \nAño: {self.anio} \nPrestado: {'prestado' if self.prestado else 'no prestado'}"
