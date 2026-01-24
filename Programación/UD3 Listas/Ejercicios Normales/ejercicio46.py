matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]
sumatoria = 0
for fila in matriz:
    for num in fila:
        sumatoria = sumatoria + num

print(sumatoria)

#Con sum

sumatoria = 0
for fila in matriz:
    sumatoria = sumatoria + sum(fila)

print(sumatoria)