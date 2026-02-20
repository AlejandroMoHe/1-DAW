def hay_negativo(lista):
    encontrado = False
    for x in lista:
        if x < 0:
            encontrado = True
    return encontrado