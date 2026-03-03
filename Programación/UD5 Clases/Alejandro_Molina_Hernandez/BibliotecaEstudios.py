from EstudiosAnima import Estudio
from datetime import date

class BibliotecaEstudios:
    def __init__(self, id: int, titulo: str, estudios: list[Estudio]):
        self.id = id
        self.titulo = titulo
        self.estudios = estudios if estudios else []
    

    def añadir_estudio(self, estudio: Estudio) -> None:
        self.estudios.append(estudio)
    

    def eliminar_estudio(self, id: int) -> bool:
        for e in self.estudios:
            if e.id == id:
                self.estudios.remove(e)
                return True
        return False
    

    def actualiza_estado(self, id: int, cambio: bool) -> bool:
        for e in self.estudios:
            if e.id == id:
                e.abierto = cambio
                return True
        return False


    def cambia_nombre(self, nuevo: str, eleccion: int) -> bool:
        for e in self.estudios:
            if eleccion == e.id:
                e.nombre = nuevo
                return True
        return False


    def mayor_ganancia(self):
        return max(self.estudios, key=lambda e: e.ganancias)
    

    def menor_ganancia(self):
        return min(self.estudios, key=lambda e: e.ganancias)


    def ordenar_apertura(self):
        return sorted(self.estudios, key=lambda e: e.fecha_apertura)


    def ordenar_ganancias(self):
        return sorted(self.estudios, key=lambda e: e.ganancias)


    def ordenar_nombre(self):
        return sorted(self.estudios, key=lambda e: e.nombre)
    

    def años_abierto(self):
        resultado = []

        for e in self.estudios:
            if e.fecha_cierre is None:
                años = (date.today() - e.fecha_apertura).days // 365
            else:
                años = (e.fecha_cierre - e.fecha_apertura).days // 365

            resultado.append((e, años))
        return resultado


    def estudios_antiguos(self, año):
        return [e for e in self.estudios if e.fecha_apertura.year < año]


    def __str__(self):
        str_biblioteca = f"{self.id} | {self.titulo}"
        print()
        for e in self.estudios:
            str_biblioteca += f"{e}\n"
        return str_biblioteca
