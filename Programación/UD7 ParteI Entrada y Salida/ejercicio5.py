with open("quijote.txt", "r", encoding="utf-8") as f:
    contador = 0
    lineas_total = 0
    for linea in f:
        lineas_total += 1
        for caracter in linea:
            contador += 1

    media = contador / lineas_total