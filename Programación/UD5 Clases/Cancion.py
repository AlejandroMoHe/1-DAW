from datetime import datetime


class Cancion:

    def __init__(self, id: int, titulo: str, artistas: list[str], album: str, generos: list[str], duracion: int, fecha_salida: datetime):
        self.id = id
        self.titulo = titulo
        self.artistas = artistas
        self.album = album
        self.generos = generos
        self.duracion = duracion
        self.fecha_salida = fecha_salida
    
    def __str__(self):
        return (
            f"Titulo: {self.titulo}\n"
            f"Artistas: {self.artistas}\n"
            f"Duración: {self.duracion}\n"
        )
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Cancion):
            return self.id == other.id