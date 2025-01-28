class Persona:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def __str__(self):
        return f"Persona: {self.nombre}, Edad: {self.edad}, Tipo: {self.tipo}"

class EmpleadoNormal(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, 'empleado_normal')

class Directivo(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, 'directivo')
