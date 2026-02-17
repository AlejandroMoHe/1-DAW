from datetime import datetime 


class Estudio:
    def __init__(self, id: int, nombre: str, fundadores: list[str], fecha_apertura: datetime, abierto: bool, ganancias: float, ultimo_estreno: datetime) -> None:
        self.id = id
        self.nombre = nombre
        self.fundadores = fundadores
        self.fecha_apertura = fecha_apertura
        self.abierto = abierto
        self.ganancias = ganancias
        self.ultimo_estreno = ultimo_estreno

    
    def __eq__(self, other) -> bool:
        if isinstance(other, Estudio):
            return self.id == other.id
        return False
    

    def __str__(self):
        return f"ID: {self.id} | {self.nombre} | {self.ganancias} millones (€)"