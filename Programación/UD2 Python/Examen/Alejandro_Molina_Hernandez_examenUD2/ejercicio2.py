precio = 0

electrica = input("Quieres que la bici sea electrica (S/N)? ")
while electrica != "S" or electrica != "N":
    if electrica == "S" or electrica == "N":
        break
    electrica = input("Valor no válido. Por favor, especifíca S o N: ")

tamaño = int(input("Que tamaño de llanta? "))
while tamaño < 12 or tamaño > 29:
    if tamaño >= 12 and tamaño <= 29:
        break
    tamaño = int(input("Número no válido. Por favor, especifíca un número válido: entre 12 y 29 ambos inclusive: "))

dias = int(input("Cuantos dias? "))
while dias < 1 or dias > 7:
    if dias >= 1 and dias <= 7:
        break
    dias = int(input("Número no válido. Por favor, especifíca un número válido: entre 1 y 7 ambos inclusive: "))

if electrica == "S":
    if tamaño <20 :
        precio = (precio + 30) *dias
    elif tamaño >=20 and tamaño<= 27.5:
        precio = (precio + 70) *dias
    else:
        precio = (precio + 100) *dias

else:
    if tamaño <20 :
        precio = (precio + 15) *dias
    elif tamaño >=20 and tamaño<= 27.5:
        precio = (precio + 30) *dias
    else:
        precio = (precio + 45) *dias

if dias >4:
    precio = (precio * 0.5) *dias

print(f"Tiene que pagar {round(precio,2)}")

