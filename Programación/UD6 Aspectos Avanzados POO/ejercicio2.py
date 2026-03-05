from datetime import datetime


class Empleado:
    def __init__(self, nombre: str, fecha_inicio: datetime, sueldo: float):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.sueldo = sueldo

class EmpleadoFijo(Empleado):
    def __init__(self, nombre: str, fecha_inicio: datetime, sueldo: float):
        super().__init__(nombre, fecha_inicio, sueldo)
    
    def trineos(self) -> int:
        hoy = datetime.today()
        antiguedad = (hoy - self.fecha_inicio).days // 365.25
        return antiguedad // 3
        


class EmpleadoTemporal(Empleado):
    def __init__(self, nombre: str, fecha_inicio: datetime, sueldo: float, fecha_fin: datetime):
        super().__init__(nombre, fecha_inicio, sueldo)
        self.fecha_fin = fecha_fin
    
    def meses_restantes(self) -> int:
        pass
        

    def ampliar_contrato(self, meses: int) -> None:
        pass

    
if __name__ == "__main__":
    fijo = EmpleadoFijo("Juan", 2022-5-14, 1200)
    temporal = EmpleadoTemporal("Maria", 2024-8-7, 1000, 2026-3-12)

    #temporal.ampliar_contrato(8)
    temporal.meses_restantes()