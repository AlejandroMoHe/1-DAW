import statistics
numeros = []
while True:
    num = int(input("Inserta un número: "))

    if num == 0:
        break
    else:
        numeros.append(num)

print(f"El número mayor es {max(numeros)}")
print(f"El número menor es {min(numeros)}")
print(f"La media de la lista es {statistics.mean(numeros)}")
    
