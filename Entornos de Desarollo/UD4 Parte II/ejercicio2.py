def contar_superiores(valores, porcentaje):
    contador = 0
    for v in valores:
        limite = max(valores) * porcentaje
        if v > limite:
            contador += 1
    return contador