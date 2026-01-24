palabras = {
   'yes': 'si',
   'cat': 'gato',
   'horse': 'caballo'
}

while True:
    palabra= input("Palabra en inglés? ")

    if palabra.lower() in palabras:
        print(f"Traducción: {palabras[palabra]}")
    else:
        print("La palabra no esta en el diccionario")
        pEspanol = input("Traducción en español? ")
        pIngles = palabra
        palabras[pIngles] = pEspanol
