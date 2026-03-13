from Curso import Curso
from random import randint


class CursoOnline(Curso):

    PRECIO_CREDITO = 10

    def __init__(self, id: int, nombre: str, creditos: int, profesor: str, alumnos: list[int] | None, plazas_totales: int, plataforma: str, url: str) -> None:
        super().__init__(id, nombre, creditos, profesor, alumnos, plazas_totales)
        self.plataforma = plataforma
        self.url = url
    
    
    def calcular_coste(self) -> float:
        return self.creditos * CursoOnline.PRECIO_CREDITO


    def generar_reunion(self) -> str:
        return f"{self.url}/{randint(1000000000, 9999999999)}"


    def __str__(self):
        base = super().__str__()
        return f"{base} | Tipo: Online | Plataforma: {self.plataforma} | Coste: {self.calcular_coste()}€"