#D
from Mano import Mano
from Baraja import Baraja

b = Baraja()

while True:
    if len(b.mazo) < 5:
        print("Sin cartas suficientes. Fin.")
        break

    opcion = input("1 = robar | 0 = salir: ")
    if opcion == "0":
        break
    if opcion != "1":
        continue

    cartas = b.mostrar(5)
    if cartas is None:
        print("Sin cartas suficientes. Fin.")
        break

    mano = Mano(cartas)
    print(mano)
    print(mano.ordenar_mano())
    print(mano.jugada())