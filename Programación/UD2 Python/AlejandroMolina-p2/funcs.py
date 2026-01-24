import random

def imprimirMenu():
    print("Bienvenido a Calculatrón 2.0!!!")
    print("1. Jugar")
    print("2. Configuración")
    print("3. Estadísticas")
    print("4. Logros")
    print("0. Salir")

def generarCuenta(numMin: int, numMax: int) -> int:
    num1 = random.randint(numMin, numMax)
    num2 = random.randint(numMin, numMax)
    operador = random.randint(0, 2)

    if operador == 0:
        resultado = num1 + num2
        respuesta = int(input(f"{num1} + {num2} = ? "))
    elif operador == 1:
        resultado = num1 - num2
        respuesta = int(input(f"{num1} - {num2} = ? "))
    else:
        resultado = num1 * num2
        respuesta = int(input(f"{num1} x {num2} = ? "))
    
    return respuesta, resultado