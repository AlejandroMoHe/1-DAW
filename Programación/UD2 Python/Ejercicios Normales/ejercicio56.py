def cuentaPalabras(frase: str) -> int:
    numPalabras = 1
    for caracter in frase:
        if caracter == " ":
            numPalabras = numPalabras + 1
    return numPalabras

frase = input("Inserta una frase: ")
numPalabras = cuentaPalabras(frase)
print(f"La frase tiene {numPalabras} palabras")