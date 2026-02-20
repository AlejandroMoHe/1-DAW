def resumen_edades(edades):
    minimo = min(edades)
    maximo = max(edades)

    suma = 0
    for e in edades:
        suma += e

    return minimo, maximo, suma