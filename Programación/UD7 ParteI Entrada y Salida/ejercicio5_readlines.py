with open("quijote.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()

lineas_mas_larga = max(lineas, key=lambda l: len(l))

print(f"El Quijote tiene {lineas_mas_larga} líneas en total")