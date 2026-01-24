import funcs

numVidas = 3
numMin = 1
numMax = 10
numAciertos = 0
numFallos = 0
rachaMaxima = 0
contPartidas = 0
respuesta = 0
logroBronce = False
logroPlata = False
logroOro = False


while True:
    
    funcs.imprimirMenu()
    opcionMenu = int(input("Selecciona una opción: "))
    
    if opcionMenu == 0:
        break

    elif opcionMenu == 1:
        contPartidas = contPartidas + 1
        vidas = numVidas
        racha = 0
        aciertosPartida = 0
        fallosPartida = 0

        while vidas > 0:
            
            respuesta, resultado = funcs.generarCuenta(numMin, numMax)

            if respuesta == resultado:
                numAciertos = numAciertos + 1
                aciertosPartida = aciertosPartida + 1
                racha = racha + 1
                print("Correcto!")
            else:
                if racha > rachaMaxima:
                    rachaMaxima = racha

                vidas = vidas - 1
                fallosPartida = fallosPartida + 1
                numFallos = numFallos + 1
                racha = 0
                print(f"Incorrecto, el resultado era {resultado}")
                print(f"Te quedan {vidas} vidas")

            if logroBronce == False and racha == 3:
                print("LOGRO DE BRONCE DESBLOQUEADO!!!")
                logroBronce = True

            if logroPlata == False and racha == 7:
                print("LOGRO DE PLATA DESBLOQUEADO!!!")
                logroPlata = True

            if logroOro == False and racha == 10:
                print("LOGRO DE ORO DESBLOQUEADO!!!")
                logroOro = True

        numFallos = numFallos + 1
        print(f"En tu partida número {contPartidas} has acertado {aciertosPartida} y has fallado {fallosPartida}")
        print(f"Has acertado un {round(aciertosPartida / (aciertosPartida + fallosPartida)*100,2)}% de las cuentas")

    elif opcionMenu == 2:
        print("La configuración actual es:")
        print(f"Número de vidas: {numVidas}")
        print(f"Número mínimo: {numMin}")
        print(f"Número máximo: {numMax}")
        print("1. Cambiar número de vidas")
        print("2. Cambiar número mínimo")
        print("3. Cambiar número máximo")
        print("0. Salir")
        opcionConf = input("¿Qué deseas hacer? ")

        if opcionConf == "1":
            numVidas = int(input("Inserta el nuevo número de vidas (Entre 1 y 10): "))

            while numVidas < 1 or numVidas > 10:
                numVidas= int(input("Número no válido, ha de ser entre 1 y 10: "))

        elif opcionConf == "2":
            numMin = int(input("Introduce el número mínimo: "))

            while numMin > numMax:
                numMin= int(input("El número mínimo ha de ser menor al número máximo: "))

        elif opcionConf == "3":
            numMax = int(input("Introduce el número máximo: "))

            while numMax < numMin:
                numMax= int(input("El número máximo ha de ser mayor al número mínimo: "))
    
    elif opcionMenu == 3:
        print(f"Has jugado un total de {contPartidas} partidas")
        print(f"Habiendo realizado un total de {numAciertos + numFallos}")
        print(f"Has acertado un total de {numAciertos} operaciones")
        print(f"Tu porcentaje de aciertos es del {round(numAciertos / (numAciertos + numFallos) *100, 2)}%")
        print(f"Has fallado un total de {numFallos} operaciones")
        print(f"Tu porcentaje de fallos es del {round(numFallos / (numAciertos + numFallos) *100, 2)}%")
        print(f"Tu racha máxima de aciertos consecutivos es: {rachaMaxima} aciertos")
    
    elif opcionMenu == 4:
        if logroBronce == False:
            estadoBronce = "NO conseguido :("
        else:
            estadoBronce = "OBTENIDO"

        if logroPlata == False:
            estadoPlata = "NO conseguido :("
        else:
            estadoPlata = "OBTENIDO"

        if logroOro == False:
            estadoOro = "NO conseguido :("
        else:
            estadoOro = "OBTENIDO"
        print(f"Logro de Bronce: Acierta tres operaciones consecutivas en una misma partida --> {estadoBronce} ")
        print(f"Logro de Plata: Acierta siete operaciones consecutivas en una misma partida --> {estadoPlata} ")
        print(f"Logro de Oro: Acierta diez operaciones consecutivas en una misma partida --> {estadoOro} ")
