numSecreto = 6
contador = 1
haAcertado = False
while not haAcertado:
    numInser= int(input("Inserta un numero: "))

    if numInser == numSecreto:
        print(f"Felicidades lo has acertado en {contador} intentos")
        haAcertado = True
    elif numInser>numSecreto:
        print("El numero secreto es menor")
    else :
        print("El numero secreto es mayor")

    contador = contador + 1
