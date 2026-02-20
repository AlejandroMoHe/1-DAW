def hay_duplicados_horror(lista):
    duplicado = False
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j and lista[i] == lista[j]:
                duplicado = True
    return duplicado