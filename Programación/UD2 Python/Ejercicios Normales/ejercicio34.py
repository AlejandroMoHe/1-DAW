numSecret = 64
nIntentos = 1
correcto = False

while not correcto:
    num = int(input("Inserta un numero: "))

    if num == numSecret:
        print(f"Has acertado! en {nIntentos} intentos")
        correcto = True
    elif num < numSecret:
        print("Incorrecto el numero es mayor")
    else:
        print("Incorrecto el numeor es menor")
    nIntentos = nIntentos + 1