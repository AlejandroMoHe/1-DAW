alumnos = [
    ["Juanillo", 4, 1, 5],
    ["Marta", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]
media =[]

for fila in alumnos:
    notas = fila[1:]
    media.append(sum(notas) / len(notas))

mediaClase = sum(media) / len(media)
print(f"La media de la clase es: {mediaClase}")