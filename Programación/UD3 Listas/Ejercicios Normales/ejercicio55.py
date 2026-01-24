import random

def crearMatriz(n: int, m: int, a: int, b: int) ->list[list[int]]:
    resultado = []
    for _ in range(n):
        resultado.append([random.randint(a,b) for _ in range(m)])
    return resultado

def imprimirMatriz(m: list[list[int]]):
    for fila in m:
        for e in fila:
            print(e, end=" ")
        print("")

imprimirMatriz(crearMatriz(2, 3, 5, 10))



