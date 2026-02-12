from datetime import datetime


class Cancion:

    def __init__(self, id: int, titulo: str, artistas: list[str], album: str, generos: list[str], duracion: int, fecha_salida: datetime) -> None:
        self.id = id
        self.titulo = titulo
        self.artistas = artistas
        self.album = album
        self.generos = generos
        self.duracion = duracion
        self.fecha_salida = fecha_salida
    

    def __eq__(self, other) -> bool:
        if isinstance(other, Cancion):
            return self.id == other.id
        return False
    

    def __str__(self):
        if len(self.artistas) > 1:
            str_artistas = ", ".join(self.artistas[:-1])
            str_artistas += f" y {self.artistas[-1]}"
        else:
            str_artistas = self.artistas[0]
        return f"{self.titulo} -- {str_artistas}"