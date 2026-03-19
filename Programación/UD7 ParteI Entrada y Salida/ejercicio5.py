linea_mas_larga = ""
max_longitud = 0

with open("quijote.txt", "r", encoding="utf-8") as f:
    for linea in f:
        longitud = len(linea)
        if longitud > max_longitud:
            max_longitud = longitud
            linea_mas_larga = linea