texto = "Hola como estas?"
palabras = 1
for letra in texto:
    if letra == " ":
        palabras = palabras + 1

print(palabras)