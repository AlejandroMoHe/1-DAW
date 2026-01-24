import random

def lanzarMoneda():
    lado = random.randint(0, 1)
    if lado == 0:
        print("cara")
    else:
        print("cruz")

    return cara

def lanzarMonedas(n:int):
    for i in range(n):
        lanzarMoneda()

def lanzarDado():
    n = random.randint(0, 6)
    #Otra Manera de hacerlo

    #n = random.random()
    #if n<=1/6:
    #    resultado = 1
    #elif n>1/6 and n <=2/6:
    #    resultado = 2
    #elif n>2/6 and n <=3/6:
    #    resultado = 3
    #elif n>3/6 and n <=4/6:
    #    resultado = 4
    #elif n>4/6 and n <=5/6:
    #    resultado = 5
    #else:
    #    resultado = 6
    print(cara)
    
    return cara

def lanzarDados(n:int):
    for i in range(n):
        lanzarDado()
