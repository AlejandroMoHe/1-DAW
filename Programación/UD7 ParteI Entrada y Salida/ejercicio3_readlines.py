with open("quijote.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()
    contador = len([linea for linea in lineas])


print(f"El Quijote tiene {contador} líneas en total")