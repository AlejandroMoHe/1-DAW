from pathlib import Path
import random


configuracion = Path(__file__).parent / "config.txt"
records = Path(__file__).parent / "records.txt"

while True:

    minimo = 0
    maximo = 0
    vidas = 0
    operador = []

    with open(configuracion, "r", encoding="utf-8") as f:
    
        for linea in f:
            separados = linea.split("=")

            if separados[0] == "min":
                minimo = int(separados[1])
            elif separados[0] == "max":
                maximo = int(separados[1])
            elif separados[0] == "operaciones":
                operador = separados[1].split(",")
            elif separados[0] == "n_vidas":
                vidas = int(separados[1])

    print(
        "-- MENU --\n"
        "1. Jugar\n"
        "2. Configuración\n"
        "3. Ver ranking\n"
        "4. Salir\n"
    )
    opcion = int(input("Elige una opción: "))

    if opcion == 4:
        print("Saliendo del programa...")
        break

    elif opcion == 1:
        num_aciertos = 0
        respuesta = None
        resultado = 0
        while vidas > 0:
            num1 = random.randint(minimo, maximo)
            num2 = random.randint(minimo, maximo)
            
            operador_juego = random.choice(operador)

            if operador_juego == "+":
                resultado = num1 + num2
                respuesta = int(input(f"{num1} + {num2} = ? "))

            elif operador_juego == "-":
                resultado = num1 - num2
                respuesta = int(input(f"{num1} - {num2} = ? "))

            elif operador_juego == "*":
                resultado = num1 * num2
                respuesta = int(input(f"{num1} x {num2} = ? "))
            
            if respuesta == resultado:
                num_aciertos += 1
                print("Correcto!")
            else:
                vidas -= 1
                print(f"Incorrecto, el resultado era {resultado}")
                print(f"Te quedan {vidas} vidas")

        nombre = input("Escribe tu nombre: ")
        with open(records, "a", encoding="utf-8") as f:
                f.write(f"{nombre}={num_aciertos}")

        print("Record guardado!!")

    elif opcion == 2:
        while opcion_config != 0:
            print("-- CONFIGURACION ACTUAL --\n")
            print(f"1. Número minimo: {minimo}")
            print(f"2. Número máximo: {maximo}")
            print(f"3. Número de vidas: {vidas}")
            print("0. Salir")
            opcion_config = int(input("Que quieres configurar"))


    elif opcion == 3:
        with open(records, "r", encoding="utf-8") as f:
                for linea in f:
                    print(linea)