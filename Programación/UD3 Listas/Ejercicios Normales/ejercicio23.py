numsInsertados = []

while True:
    num = int(input("Inserta un número: "))
    
    if num >= 0:
        numsInsertados.append(num)
    else:
        numsInsertados.remove(num*-1)

    print(f"Números Introducidos: {numsInsertados}")