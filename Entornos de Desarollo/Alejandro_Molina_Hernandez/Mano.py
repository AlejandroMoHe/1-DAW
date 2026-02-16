#B
from collections import Counter
from Carta import Carta

class Mano:
    def __init__(self, mano: list[Carta]):
        self.mano = mano

    def ordenar_mano(self) -> tuple[int, int]:
        valor_ordenado = sorted([c.num for c in self.mano])
        palos = [c.palo for c in self.mano]
        num_total = Counter(valor_ordenado)
        palos_total = Counter(palos)

        es_color = len(palos_total) == 1
        es_escalera = valor_ordenado == list(range(valor_ordenado[0], valor_ordenado[0] + 5))

        if es_escalera and es_color:
            return (8, max(valor_ordenado))
        if 4 in num_total.values():
            return (7, max(k for k, valor in num_total.items() if valor == 4))
        if sorted(num_total.values()) == [2, 3]:
            return (6, max(k for k, valor in num_total.items() if valor == 3))
        if es_color:
            return (5, max(valor_ordenado))
        if es_escalera:
            return (4, max(valor_ordenado))
        if 3 in num_total.values():
            return (3, max(k for k, valor in num_total.items() if valor == 3))
        if list(num_total.values()).count(2) == 2:
            return (2, max(k for k, valor in num_total.items() if valor == 2))
        if 2 in num_total.values():
            return (1, max(k for k, valor in num_total.items() if valor == 2))
        return (0, max(valor_ordenado))
    
    def jugada(self) -> str:
        t, _ = self.ordenar_mano()
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
        ][t]

    def __str__(self):
        return " ".join(str(carta) for carta in self.a1)