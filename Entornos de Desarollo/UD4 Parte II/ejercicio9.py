def contar_mas_largos_horror(textos):
    contador = 0
    for t in textos:
        suma = 0
        for x in textos:
            suma += len(x)
        media = suma / len(textos)

        if len(t) > media:
            contador += 1

    return contador