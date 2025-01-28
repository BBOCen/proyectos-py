import os
import pickle

class SistemaGestionTareas:
    def __init__(self):
        self.usuarios = []
        self.cargar_datos()

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    #Este método carga los datos de las tareas guardadas
    def cargar_datos(self):
        if os.path.exists("tareas.dat"):
            with open("tareas.dat", "rb") as archivo:
                self.usuarios = pickle.load(archivo)

    #Este método guarda los datos de las tareas
    def guardar_datos(self):
        with open("tareas.dat", "wb") as archivo:
            pickle.dump(self.usuarios, archivo)

    def imprimir_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)

    def buscar_usuario(self, nombre):
        for usuario in self.usuarios:
            if usuario.nombre.lower() == nombre.lower():
                return usuario
        return None

    def buscar_proyecto(self, usuario, nombre_proyecto):
        for proyecto in usuario.proyectos:
            if proyecto.nombre.lower() == nombre_proyecto.lower():
                return proyecto
        return None

    def buscar_tarea(self, proyecto, titulo_tarea):
        for tarea in proyecto.tareas:
            if tarea.titulo.lower() == titulo_tarea.lower():
                return tarea
        return None