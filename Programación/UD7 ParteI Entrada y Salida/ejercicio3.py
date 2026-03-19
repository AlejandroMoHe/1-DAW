with open("quijote.txt", "r", encoding="utf-8") as f:
    contador = 0
    for linea in f:
        linea = linea.lower()
        contador += linea.count("caballero")
        


print(f"El Quijote tiene {contador} líneas que contiene caballero")