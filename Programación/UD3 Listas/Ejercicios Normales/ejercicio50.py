matriz = [
    ["Perro", "Gato", "Hámster"],
    ["Loro", "Conejo", "Tortuga"],
    ["Pez", "Hurón", "Ardilla"],
    ["Iguana", "Serpiente", "Erizo"]
]

numAnimales = 0

for fila in matriz:
    for animal in fila:
        if animal[0].lower() in ["a","e","i","o","u"]:
            numAnimales = numAnimales + 1

print(f"Hay un total de {numAnimales} animales que empiezan por vocal") 