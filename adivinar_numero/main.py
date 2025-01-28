import random

aleatorio = random.randint(0, 20)
salir = False
intentos = 3

while not salir:
    try:
        print(aleatorio)
        num_introducido = int(input(f"Introduce el número que tú crees que podría ser el aleatorio (el número está entre 0 y 20). Tienes {intentos} intento(s): "))

        if intentos==1:
            print(f"Has perdido, el número era: {aleatorio}")
            salir = True

        elif num_introducido==aleatorio:
            print("Muy bien! Ese es el número")
            salir = True

        elif abs(aleatorio - num_introducido) <= 5:
            intentos -= 1
            print(f"No es el número aleatorio, pero estás muy cerca.")

        else:
            intentos -= 1
            print(f"Ese no es el número aleatorio.")

    except ValueError:
        print("Introduce un número válido")
