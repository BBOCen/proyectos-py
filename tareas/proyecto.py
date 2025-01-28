class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def __str__(self):
        return f"Proyecto: {self.nombre}\nTareas: \n" + "\n".join([str(tarea) for tarea in self.tareas])