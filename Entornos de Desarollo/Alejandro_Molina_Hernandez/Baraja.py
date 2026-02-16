#C
import random
from Carta import Carta

class Baraja:
    def __init__(self):
        self.mazo = [Carta(valor, palo) for valor in range(2, 15) for palo in ["♠", "♥", "♦", "♣"]]
        random.shuffle(self.mazo)

    def robar_carta(self):
        if not self.mazo:
            return None
        return self.mazo.pop()

    def mostrar(self, num: int):
        if len(self.mazo) < num:
            return None
        return [self.robar_carta() for _ in range(num)]