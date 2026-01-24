palabraMayor = ""
palabraMenor = ""
i = 1
while True:
    palabra = input("Inserta una palabra: ")
    if palabra == "fin":
     break

    if i == 1:
        palabraMayor = palabra
        palabraMenor = palabra
    else:
        if len(palabra) >= len(palabraMayor):
            palabraMayor = palabra
            
        elif len(palabra) <= len(palabraMenor):
            palabraMenor = palabra
    i = i + 1
print(f"La palabra más corta es: {palabraMenor} y la más larga es: {palabraMayor}")