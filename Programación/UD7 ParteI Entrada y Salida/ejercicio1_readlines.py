with open("quijote.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()
    contador = len(lineas)


print(f"El Quijote tiene {contador} líneas en total")