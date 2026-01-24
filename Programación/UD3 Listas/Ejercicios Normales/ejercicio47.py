matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]

#Sin usar index
posFila = posColumna = None
for i, fila in enumerate(matriz):
    for j, num in enumerate(fila):
        if num == 5:
            posFila = i
            posColumna = j

print(f"La posición del último 5 es: {posFila} {posColumna}")
        
#Usando index
posFila = posColumna = None

for i, fila in enumerate(matriz):
    if fila.count(5) > 0:
        posFila = i
        posColumna = fila.index(5)

print(f"La posición del último 5 es: {posFila} {posColumna}")