matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]

for i, fila in enumerate(matriz):
    for j, num in enumerate(fila):
        if num < 0:
            matriz[i][j] = matriz[i][j] * -1

print(matriz)
        