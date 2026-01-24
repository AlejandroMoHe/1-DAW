alumnos = [
    ["Juanillo", 4, 1, 5],
    ["Marta", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]

media =[]

for fila in alumnos:
    notas = alumno[1:]
    media.append(sum(notas) / len(notas))

mediaMinima = min(media)
posMinima = media.index(mediaMinima)
print(f"El alumno con peor nota media {mediaMinima} es : {alumnos}")