from datetime import datetime


class Vehiculo:
    def __init__(self, matricula: int, marca: str, fecha_matriculacion: datetime, fecha_ultima_itv: datetime) -> None:
        self.matricula = matricula
        self.marca = marca
        self.fecha_matriculacion = fecha_matriculacion
        self.fecha_ultima_itv = fecha_ultima_itv


class Coche(Vehiculo):
    def __init__(self, matricula: int, marca: str, fecha_matriculacion: datetime, fecha_ultima_itv: datetime, num_puertas: int, combustible: str ):
        super().__init__(matricula, marca, fecha_matriculacion, fecha_ultima_itv)
        self.num_puertas = num_puertas
        self.combustible = combustible
    
    def proxima_itv(self) -> datetime:
        return self.fecha_ultima_itv


class Moto(Vehiculo):
    def __init__(self, matricula: int, marca: str, fecha_matriculacion: datetime, fecha_ultima_itv: datetime, cilindrada: int):
        super().__init__(matricula, marca, fecha_matriculacion, fecha_ultima_itv)
        self.cilindrada = cilindrada

    def proxima_itv() -> datetime:
        pass

if __name__ == "__main__": 
    pass