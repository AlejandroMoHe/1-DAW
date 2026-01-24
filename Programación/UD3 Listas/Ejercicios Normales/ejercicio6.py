import random

#Esto genera mil número aleatrorios entre 0 y 10
aleatorios = [random.randint(10) for _ in range(1000)]

mayor = aleatorios[0]

for n in aleatorios:
    if n > mayor:
        mayor = n
print(f"El mayor es {mayor}")