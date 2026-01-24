def mayor_igual(lista: list, n: int) -> bool:
    return n <= min(lista)

lista = [4,7,5,10,12]
n = 2

print(mayor_igual(lista, n))