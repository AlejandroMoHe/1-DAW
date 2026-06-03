from Banda import Banda


class Vinilo:
    def __init__(self, id: int, nombre: str, banda: Banda):
        self.id = id
        self.nombre = nombre
        self.banda = banda

    def __str__(self):
        return f"{self.id} - {self.nombre} ({self.banda.nombre})"