class Prestamo:
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario

    def __str__(self):
        return f"Préstamo: \nDatos usuario: {self.usuario} \nDatos libro: {self.libro}"