import random

def operadorAleatorio (randint: int):
    ope = random.randint(0, 3)


def cuenta(incio: int, final: int) -> int:
    num1 = random.randint(0, 11)
    num2 = random.randint(0, 11)
    operador = operadorAleatorio()

    if operador == 0:
        calculo = num1 + num2
    elif operador == 1:
        calculo = num1 - num2
    else:
        calculo = num1 * num2
    
    print()

inicio = 1
final = 10
for i in range(10):
    respuesta = (input(f"Cuanto es {cuenta}: "))
    
    if respuesta == calculo:
        print("Has acertado")
    else:
        print("Has fallado")

