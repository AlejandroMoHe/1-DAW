with open("quijote.txt", "r", encoding="utf-8") as f:
    contador_letra = 0
    lineas_total = 0
    for linea in f:
        lineas_total += 1
        for caracter in linea:
            contador_letra += 1

    media = contador_letra / lineas_total


print(f"El Quijote tiene {media} media de caracteres por linea")