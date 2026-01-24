texto = "Hola como estas?"
nVeces = 0

for letra in texto:
    if letra == "a" or letra=="e" or letra=="i" or letra=="o" or letra=="u" or letra == "A" or letra=="E" or letra=="I" or letra=="O" or letra=="U":
        nVeces = nVeces + 1
print(nVeces)