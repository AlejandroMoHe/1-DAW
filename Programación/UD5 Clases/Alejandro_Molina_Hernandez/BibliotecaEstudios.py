from EstudiosAnima import Estudio

class BibliotecaEstudios:
    def __init__(self, id: int, titulo: str, estudios: list[Estudio]):
        self.id = id
        self.titulo = titulo
        self.estudios = estudios
    

    def añadir_estudio(self, e: Estudio) -> None:
        self.estudios.append(e)
    
    def eliminar_estudio(self, id: int) -> bool:
        for e in self.estudios:
            if e.id == id:
                self.estudios.remove(e)
                return True
        return False
    
    def actualiza_estado(self):
        pass

    def cambia_nombre(self):
        pass

    def menor_ganacia(self):
        pass

    def ordenar_apertura(self):
        pass

    def tiempo_abierto(self):
        pass

    def estreno_hoy(self):
        pass

    def __str__(self):
        pass