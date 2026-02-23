import random
from Carta import Carta


class Baraja:
    """
    Clase que representa una baraja de cartas.

    Genera una baraja y las mezcla.
    """

    def __init__(self):
        """
        Crea la baraja y las mezcla de forma aleatoria.
        """
        self.cartas = [
            Carta(valor, palo)
            for valor in range(2, 15)
            for palo in ["♠", "♥", "♦", "♣"]
        ]
        random.shuffle(self.cartas)

    def robar_carta(self) -> Carta | None:
        """
        Roba una carta de la baraja.

        :return: Carta robada o None si la baraja está vacía
        """
        if not self.cartas:
            return None
        return self.cartas.pop()

    def robar_cartas(self, cantidad: int) -> list[Carta] | None:
        """
        Roba varias cartas de la baraja.

        :param cantidad: Número de cartas para robar
        :return: Lista de cartas o None si no hay suficientes cartas
        """
        if len(self.cartas) < cantidad:
            return None
        return [self.robar_carta() for _ in range(cantidad)]
