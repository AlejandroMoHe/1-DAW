with open("quijote.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()
    contador = len([linea for linea in lineas for palabra in linea.split(" ") if palabra == "Don"])

print(f"El Quijote tiene {contador} líneas que empiezan con la palabra Don")