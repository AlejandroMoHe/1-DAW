#A
class Carta:
    def __init__(self, num: int, palo: str):
        self.num = num
        self.palo = palo

    def __str__(self):
        valor = {11: "J", 12: "Q", 13: "K", 14: "A"}
        return f"{valor.get(self.num, self.num)}{self.palo}"