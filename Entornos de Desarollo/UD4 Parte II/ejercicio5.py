def contar_letras(texto):
    res = []
    for c in texto:
        encontrado = False
        for i in range(len(res)):
            if res[i][0] == c:
                res[i] = (c, res[i][1] + 1)
                encontrado = True
        if not encontrado:
            res.append((c, 1))
    return res