from proyecto import Proyecto
from sistema_gestion import SistemaGestionTareas
from usuario import Usuario
from tarea import Tarea
from datetime import datetime

def mostrar_menu():
    print("\n---- Menú ----")
    print("1. Agregar usuario")
    print("2. Agregar proyecto a usuario")
    print("3. Agregar tarea a proyecto")
    print("4. Marcar tarea como completa")
    print("5. Mostrar todos los usuarios")
    print("6. Mostrar tareas de un proyecto")
    print("7. Salir")

sistema = SistemaGestionTareas()

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre_usuario = input("Ingresa el nombre del usuario: ")
        usuario = Usuario(nombre_usuario)
        sistema.agregar_usuario(usuario)
        print(f"Usuario '{nombre_usuario}' agregado exitosamente.")

    elif opcion == "2":
        nombre_usuario = input("Ingresa el nombre del usuario para agregar el proyecto: ")
        usuario = sistema.buscar_usuario(nombre_usuario)
        if usuario:
            nombre_proyecto = input("Ingresa el nombre del proyecto: ")
            proyecto = Proyecto(nombre_proyecto)
            usuario.agregar_proyecto(proyecto)
            print(f"Proyecto '{nombre_proyecto}' agregado a '{nombre_usuario}'.")
        else:
            print("Usuario no encontrado.")

    elif opcion == "3":
        nombre_usuario = input("Ingresa el nombre del usuario para agregar la tarea: ")
        usuario = sistema.buscar_usuario(nombre_usuario)
        if usuario:
            nombre_proyecto = input("Ingresa el nombre del proyecto donde agregar la tarea: ")
            proyecto = sistema.buscar_proyecto(usuario, nombre_proyecto)
            if proyecto:
                titulo = input("Ingresa el título de la tarea: ")
                descripcion = input("Ingresa la descripción de la tarea: ")
                prioridad = input("Ingresa la prioridad (Alta, Media, Baja): ")
                fecha_vencimiento = input("Ingresa la fecha de vencimiento (AAAA-MM-DD): ")
                fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
                tarea = Tarea(titulo, descripcion, prioridad, fecha_vencimiento)
                proyecto.agregar_tarea(tarea)
                print(f"Tarea '{titulo}' agregada al proyecto '{nombre_proyecto}'.")
            else:
                print("Proyecto no encontrado.")
        else:
            print("Usuario no encontrado.")

    elif opcion == "4":
        nombre_usuario = input("Ingresa el nombre del usuario para marcar tarea como completa: ")
        usuario = sistema.buscar_usuario(nombre_usuario)
        if usuario:
            nombre_proyecto = input("Ingresa el nombre del proyecto donde se encuentra la tarea: ")
            proyecto = sistema.buscar_proyecto(usuario, nombre_proyecto)
            if proyecto:
                titulo_tarea = input("Ingresa el título de la tarea a marcar como completa: ")
                tarea = sistema.buscar_tarea(proyecto, titulo_tarea)
                if tarea:
                    tarea.marcar_completa()
                    print(f"Tarea '{titulo_tarea}' marcada como completa.")
                else:
                    print("Tarea no encontrada.")
            else:
                print("Proyecto no encontrado.")
        else:
            print("Usuario no encontrado.")

    elif opcion == "5":
        sistema.imprimir_usuarios()

    elif opcion == "6":
        nombre_usuario = input("Ingresa el nombre del usuario para ver sus proyectos: ")
        usuario = sistema.buscar_usuario(nombre_usuario)
        if usuario:
            nombre_proyecto = input("Ingresa el nombre del proyecto: ")
            proyecto = sistema.buscar_proyecto(usuario, nombre_proyecto)
            if proyecto:
                print(f"\nProyectos y tareas de '{nombre_proyecto}':")
                print(proyecto)
            else:
                print("Proyecto no encontrado.")
        else:
            print("Usuario no encontrado.")

    elif opcion == "7":
        sistema.guardar_datos()
        print("Datos guardados. Saliendo del sistema...")
        break

    else:
        print("Opción no válida, por favor elige una opción del menú.")
