suma = 0
contador = 0
numMayor = 0
numMenor = 0
while True:
    num = int(input("Introduce un numero: "))
    contador = contador + num
    if num == 0:
        break
    else:
        suma = suma + num
        if num>suma and num != 0:
            numMayor = num
        elif num<suma and num != 0:
            numMenor = num
print(f"El numero máximo escrito es {numMayor}")
print(f"El numero menor escrito es {numMenor}")
print(f"La media aritmética de todos los numeros insertados es: {suma/contador}")