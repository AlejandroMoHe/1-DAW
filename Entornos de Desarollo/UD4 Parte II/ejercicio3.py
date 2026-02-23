def hay_negativo(lista: list) -> bool:
    encontrado = False
    for x in lista:
        if x < 0:
            encontrado = True
    return encontrado