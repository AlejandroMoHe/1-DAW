import random

def caraCruz (nVeces:int):
    for i in range(nVeces):
        lado = random.randint(0, 1)
        if lado == 0:
            print("cruz")
        else:
            print("cara")
nVeces = int(input("Cuantas monedas quieres lanzar: "))
caraCruz(nVeces)
