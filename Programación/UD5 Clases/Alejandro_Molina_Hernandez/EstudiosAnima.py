from datetime import date 


class Estudio:
    def __init__(self, id: int, nombre: str, fundadores: list[str], fecha_apertura: date, abierto: bool, fecha_cierre: date, ganancias: float, ultimo_estreno: date) -> None:
        self.id = id
        self.nombre = nombre
        self.fundadores = fundadores
        self.fecha_apertura = fecha_apertura
        self.fecha_cierre = fecha_cierre
        self.abierto = abierto
        self.ganancias = ganancias
        self.ultimo_estreno = ultimo_estreno

    
    def __eq__(self, other) -> bool:
        if isinstance(other, Estudio):
            return self.id == other.id
        return False
    
    def __hash__(self):
        return self.id

    def __str__(self) -> str:
        return f"ID: {self.id} | {self.nombre} | {self.ganancias} millones (€)"