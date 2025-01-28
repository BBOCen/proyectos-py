class Usuario:
    def __init__(self, nombre, registro):
        self.nombre = nombre
        self.registro = registro

    def __str__(self):
        return f"Nombre: {self.nombre} \nRegistro: {self.registro}"
