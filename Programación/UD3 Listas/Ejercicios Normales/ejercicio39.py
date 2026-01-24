pala = input("Inserta palabras separadas por coma:")

palabras = pala.split(",")

masLarga = palabras[0]
masCorta = palabras[0]

for palabra in palabras:
    if len(palabra)>len(masLarga):
        masLarga = palabra
    
    if len(palabra)<len(masLarga):
        masCorta = palabra 

print(f"La palabra más corta es: {masCorta}")
print(f"La palabra más larga es: {masLarga}")
