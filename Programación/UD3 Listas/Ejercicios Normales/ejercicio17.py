numeros = []
total = 0

while True:
    num = int(input("Inserta un numero: "))

    total = total + num

    if num == 0:
        break
    else:
        sumatoria = 0
        numeros.append(num)

media = sumatoria /len(numeros)

print(numeros)

