class Carta:
    """
    Clase que representa una carta de una baraja.

    :param valor: Valor numérico de la carta
    :param palo: Palo de la carta
    """

    def __init__(self, valor: int, palo: str):
        """
        Crea una carta con valor y palo.

        :param valor: Valor de la carta
        :param palo: Palo de la carta
        """
        self.valor = valor
        self.palo = palo

    def __str__(self) -> str:
        """
        Devuelve la representación de la carta.

        :return: Cadena con el valor y palo de la carta
        """
        valores = {11: "J", 12: "Q", 13: "K", 14: "A"}
        return f"{valores.get(self.valor, self.valor)}{self.palo}"