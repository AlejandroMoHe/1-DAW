with open("quijote.txt", "r", encoding="utf-8") as f:
    contador = 0
    for linea in f:
        for palabra in linea.split(" "):
            if palabra.lower() == "caballero":
                contador += 1
        


print(f"El Quijote tiene {contador} líneas que contiene caballero")