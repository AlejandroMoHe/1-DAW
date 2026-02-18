from EstudiosAnima import Estudio
from datetime import datetime

class BibliotecaEstudios:
    def __init__(self, id: int, titulo: str, estudios: list[Estudio]):
        self.id = id
        self.titulo = titulo
        if len(estudios) > 0:
            self.estudios = estudios
    

    def añadir(self, e: Estudio) -> None:
        self.estudios.append(e)
    

    def eliminar_estudio(self, id: int) -> bool:
        for e in self.estudios:
            if e.id == id:
                self.estudios.remove(e)
                return True
        return False
    

    def actualiza_estado(self, opcion: int, cambio: str) -> None:
        for e in self.estudios:
            if cambio == "S" and e.id == opcion:
                e.abierto == True
            elif cambio == "N" and e.id == opcion:
                e.abierto == False


    def cambia_nombre(self, nuevo: str, eleccion: int) -> bool:
        for e in self.estudios:
            if eleccion == e.id:
                e.nombre = nuevo
                return True
            return False


    def mayor_ganacia(self):
        return max(self.estudios, key=lambda e: e.ganancias)


    def ordenar_apetura(self):
        sorted()


    def tiempo_abierto(self):
        for e in self.estudios:
            if e.abierto == True and e.fecha_cierre == None:
                print(f"{e.nombre} lleva abierto por {e.fecha_apertura - datetime.now}")
            else:
                print(f"{e.nombre} estuvo abierto por {e.fecha_apertura - e.fecha_cierre}")


    def dias_desde_estreno(self) -> datetime:
        for e in self.estudios:
            contador = e.fecha_apertura - datetime.now
            print(f"El último estreno de {e.nombre} fue hace {contador}")


    def __str__(self):
        str_biblioteca = f"{self.id} | {self.titulo}"
        for e in self.estudios:
            str_biblioteca += f"{e}\n"
        return str_biblioteca