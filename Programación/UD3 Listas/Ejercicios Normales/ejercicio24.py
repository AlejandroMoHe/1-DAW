numeros = []

while True:
    num = int(input("Inserta un número: "))

    if num == 0:
        break

    numeros.append(num)

while len(numeros) > 0:
    print(numeros.pop())

# con recursividad

#def reverso(numeros: list[int]):
#    if len(numeros) == 0:
#        return
#    else:
#        print(numeros.pop())
#        return reverso(numeros)
