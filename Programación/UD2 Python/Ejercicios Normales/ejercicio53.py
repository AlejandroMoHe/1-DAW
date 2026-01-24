def vocales(palabra: str) -> int:
    numVocales = 0
    for letra in palabra:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
            numVocales = numVocales +1
        return numVocales
palabra = input("Inserta un palabra: ")
numVocales = vocales(palabra)
print(f"La palabra insertada tiene {numVocales} vocales")