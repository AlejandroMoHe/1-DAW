from pathlib import Path


lazarillo = Path(__file__).parent / "lazarillo.txt"
analisis = Path(__file__).parent / "analisis_lazarillo.txt"

lineas = 0
palabras = 0
letras = 0
linea_mas_larga = ""
max_longitud = 0

with open(lazarillo, "r", encoding="utf-8") as f:
    
    for linea in f:
        lineas += 1
        palabras += len(linea.split(" "))
        letras += sum(letra.isalpha() for letra in linea)
        longitud = len(linea)
        if longitud > max_longitud:
            max_longitud = longitud
            linea_mas_larga = linea



with open(analisis, "w", encoding="utf-8") as f:
    f.write(f"Líneas: {lineas}\nPalabras: {palabras}\nLetras: {letras}\nLínea más larga: {linea_mas_larga}")
