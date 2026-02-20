def suma_horror(lista):
    suma = 0
    for i in range(len(lista)):
        if lista[i] < 0:
            for j in range(i):
                suma += lista[j]
            break
    return suma