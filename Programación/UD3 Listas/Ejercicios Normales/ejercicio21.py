numeros = []
while True:
    numInsertado = int(input("Inserta un numero: "))

    if numInsertado == 0:
        break

    if len(numeros) == 0:
        numeros.append(numInsertado)
    else:
        insertado = False
        for i in range(0, len(numeros)+1):
            if i< len(numeros) and numeros[i] > numInsertado:
                numeros.insert(i, numInsertado)
                insertado = True
                break

        if not insertado:
            numeros.append(numInsertado)


print(numeros)

def sumatoria_rec(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    else:
        return nums.pop() + sumatoria_rec(nums)