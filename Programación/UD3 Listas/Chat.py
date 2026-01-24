from random import randint

def matriz_aleatorio(n: int, m: int) -> list[list[int]]:
    matriz = []
    for _ in range(n):
        matriz.append([randint(0, 9) for _ in range(m)])
    return matriz

def imprimir_matriz(m: list[list[int]]):
    for fila in m:
        for n in fila:
            print(n, end=" ")
        print()

print(matriz_aleatorio(10,10))