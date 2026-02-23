from Mano import Mano
from Baraja import Baraja


def main():
    """
    Función principal que ejecuta el juego.

    El usuario roba manos de 5 cartas hasta que no queden suficientes
    cartas en la baraja o eliga salir.
    """
    baraja = Baraja()

    while True:
        if len(baraja.cartas) < 5:
            print("Sin cartas suficientes. Fin.")
            break

        opcion = input("1 = robar | 0 = salir: ")

        if opcion == "0":
            break
        if opcion != "1":
            continue

        cartas = baraja.robar_cartas(5)
        if cartas is None:
            print("Sin cartas suficientes. Fin.")
            break

        mano = Mano(cartas)

        print(mano)
        print(mano.calcular_mano())
        print(mano.nombre_mano())


if __name__ == "__main__":
    main()
