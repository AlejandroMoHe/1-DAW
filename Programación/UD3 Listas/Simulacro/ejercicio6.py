def es_cuadrada(m: list[list[int]]) -> bool:
    return len(m) == len(m[0])

matriz = [
    [5,4,2,5],
    [3,4,5,7],
    [4,8,6,4]
]

matriz2 = [
    [8,9,7,5]
    [9,1,7,6]
]

print(es_cuadrada(matriz))
print(es_cuadrada(matriz2))

