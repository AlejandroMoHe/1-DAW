from collections import Counter
from Carta import Carta


class Mano:
    """
    Clase de una mano en un juego de cartas.

    :param cartas: Lista de Cartas.
    """

    def __init__(self, cartas: list[Carta]):
        """
        Crea la mano de cartas.

        :param cartas: Lista de cartas
        """
        self.cartas = cartas

    def calcular_mano(self) -> tuple[int, int]:
        """
        Evalúa la mano.

        :return: Tupla con (ranking, valor clave)
        """
        valores = sorted([carta.valor for carta in self.cartas])
        palos = [carta.palo for carta in self.cartas]

        contado_valor = Counter(valores)
        contado_palos = Counter(palos)

        mismo_palo = len(contado_palos) == 1
        escalera = valores == list(range(valores[0], valores[0] + 5))

        if escalera and mismo_palo:
            return (8, max(valores))
        if 4 in contado_valor.values():
            return (7, max(k for k, v in contado_valor.items() if v == 4))
        if sorted(contado_valor.values()) == [2, 3]:
            return (6, max(k for k, v in contado_valor.items() if v == 3))
        if mismo_palo:
            return (5, max(valores))
        if escalera:
            return (4, max(valores))
        if 3 in contado_valor.values():
            return (3, max(k for k, v in contado_valor.items() if v == 3))
        if list(contado_valor.values()).count(2) == 2:
            return (2, max(k for k, v in contado_valor.items() if v == 2))
        if 2 in contado_valor.values():
            return (1, max(k for k, v in contado_valor.items() if v == 2))

        return (0, max(valores))

    def nombre_mano(self) -> str:
        """
        Devuelve el nombre de la jugada.

        :return: Nombre de la jugada.
        """
        rank, _ = self.calcular_mano()
        return [
            "Carta alta",
            "Pareja",
            "Doble pareja",
            "Trío",
            "Escalera",
            "Color",
            "Full",
            "Póker",
            "Escalera de color"
        ][rank]

    def __str__(self) -> str:
        """
        Representación de la mano.

        :return: Cartas separadas por espacios
        """
        return " ".join(str(carta) for carta in self.cartas)
