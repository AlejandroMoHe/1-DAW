from pathlib import Path


quijote = Path(__file__).parent / "quijote.txt"
dato_quijote = Path(__file__).parent / "datos_quijote.txt"

lineas = 0
palabras = 0
letras = 0

with open(quijote, "r", encoding="utf-8") as f:
    
    for linea in f:
        lineas += 1
        palabras += len(linea.split(" "))
        letras += sum(letra.isalpha() for letra in linea)


with open(dato_quijote, "w", encoding="utf-8") as f:
  f.write(f"El Quijote tiene {lineas} líneas {palabras} palabras y {letras} letras")