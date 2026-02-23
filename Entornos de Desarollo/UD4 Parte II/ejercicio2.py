def contar_superiores(valores: list[int], porcentaje: float) -> int:
    contador = 0

    for valor in valores:
        limite = max(valores) * porcentaje
        if valor > limite:
            contador += 1
    return contador