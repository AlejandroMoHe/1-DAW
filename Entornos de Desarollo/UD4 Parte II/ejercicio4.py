def resumen_edades(edades: list[int]) -> int:
    minimo = min(edades)
    maximo = max(edades)

    suma = 0
    for e in edades:
        suma += e

    return minimo, maximo, suma