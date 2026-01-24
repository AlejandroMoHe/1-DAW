import random

#Esto genera mil número aleatrorios entre 0 y 10
aleatorios = [random.randint(1,10) for _ in range(1000)]

menor = aleatorios[0]

for n in aleatorios:
    if n < menor:
        menor = n
print(f"El menor es {menor}")