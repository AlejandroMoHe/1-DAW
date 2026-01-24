import random
import math

inicio = float(input("Inserta un numero: "))
fin = float(input("Inserta otro numero: "))
nVeces = int(input("Cuantos numeros quieres: "))

for i in range(nVeces):
    num = random.randint(inicio, fin)

    print(num)

#inicio + ((fin-inico)*random())