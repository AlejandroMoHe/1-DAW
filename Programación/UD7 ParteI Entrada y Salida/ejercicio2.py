with open("quijote.txt", "r", encoding="utf-8") as f:
    contador = 0
    for linea in f:
        if linea[:4] == "Don ":
            contador += 1
    


print(f"El Quijote tiene {contador} líneas que empiezan por Don")