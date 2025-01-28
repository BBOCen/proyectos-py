class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.proyectos = []

    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)

    def __str__(self):
        return f"Usuario: {self.nombre}\nProyectos: \n" + "\n".join([str(proyecto) for proyecto in self.proyectos])