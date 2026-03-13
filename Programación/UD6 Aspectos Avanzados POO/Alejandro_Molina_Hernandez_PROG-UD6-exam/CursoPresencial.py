from Curso import Curso


class CursoPresencial(Curso):

    PRECIO_CREDITO = 15

    def __init__(self, id: int, nombre: str, creditos: int, profesor: str, alumnos: list[int] | None, plazas_totales: int, direccion: str, aula: str, asistencia: dict[str, list[int]] | None) -> None:
        super().__init__(id, nombre, creditos, profesor, alumnos, plazas_totales)
        self.direccion = direccion
        self.aula = aula
        self.asistencia = asistencia

    
    def calcular_coste(self) -> float:
        return self.creditos * CursoPresencial.PRECIO_CREDITO


    def pasar_lista(self, fecha: str, alumnos_presentes: list[int]) -> None:
        pass


    def __str__(self):
        base = super().__str__()
        return f"{base} | Tipo: Presencial | Aula: {self.aula} | Coste: {self.calcular_coste()}€"