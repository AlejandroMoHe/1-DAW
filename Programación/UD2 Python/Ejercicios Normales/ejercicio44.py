while True:
    numReal = float(input("Inserta un numero real: "))
    numEntero = int(input("Inserta un numero entero: "))
    if numReal == 0 or numEntero == 0:
        break
    else:
        numFinal = round(numReal, numEntero)
        print(numFinal)