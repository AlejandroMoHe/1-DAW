from pathlib import Path


ruta_fichero = Path(__file__).parent / "palabras.txt"


with open(ruta_fichero, "a", encoding="utf-8") as f:
  while True:
    palabra = input("Escribe una palabra: ")
    if palabra != "fin":
        f.write(f"{palabra}\n")
    else:
       break