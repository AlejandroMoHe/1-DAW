alumnos = [
    ["Juanillo", 4, 1, 5],
    ["Marta", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]

for alumno in alumnos:
    nombre = alumno[0]
    notas = alumno[1:]
    media = sum(notas) / len(notas)
    print(f"La nota media de {nombre} es {round(media, 1)}")