matriz = [
    ["Perro", "Gato", "Hámster"],
    ["Loro", "Conejo", "Tortuga"],
    ["Pez", "Hurón", "Ardilla"],
    ["Iguana", "Serpiente", "Erizo"]
]

animalMayor = ""

for fila in matriz:
    for animal in fila:
        if len(animal) > len(animalMayor):
         animalMayor = animal

print(animalMayor)