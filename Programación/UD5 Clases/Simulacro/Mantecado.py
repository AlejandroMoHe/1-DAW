#Ejercicio 1
from datetime import date


class Mantecado:

    def __init__(self, id: int, tipo: str, fecha_creacion: date, fecha_caducidad: date, precio: float, ingredientes: list[str]):
        self.id = id
        self.tipo = tipo
        self.fecha_creacion = fecha_creacion
        self.fecha_caducidad = fecha_caducidad
        self.precio = precio
        self.ingredientes = ingredientes
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Mantecado):
            return self.id == other.id
        return False
    
    def dias_para_caducar(self) -> int:
        dias = self.fecha_caducidad - date.today()
        return dias.days

    def esta_caducado(self) -> bool:
        if self.fecha_caducidad < date.today():
            return True
        else:
            return False

    def __str__(self):        
        return f"{self.id} - {self.tipo} - {self.fecha_creacion} - {self.fecha_caducidad} - {self.precio} - {self.ingredientes}"
    

if __name__ == '__main__':
    m1 = Mantecado(1, "Chocolate", date(2025, 12, 1), date(2025, 12, 31), 3.5, ["harina", "azúcar", "manteca", "cacao"])
    m2 = Mantecado(2, "Chocolate Especial", date(2025, 12, 5), date(2026, 1, 5), 4.0, ["harina", "azúcar", "manteca", "cacao", "almendra"])

    print(f"Representación:\n {m1}\n ")
    print(f"Días para caducar:\n {m1.dias_para_caducar()}\n ")
    print(f"Esta caducado?\n {m1.esta_caducado()}\n")
    print(f"Comparación por id (m1 == m2):\n {m1.__eq__(m2)}")