from Cancion import Cancion
import random


class Playlist:
    def __init__(self, id_playlist: int, nombre: str, canciones: list[Cancion]):
        self.id_playlist = id_playlist
        self.nombre = nombre
        self.canciones = canciones
    
    def __str__(self):
        return(
            f"ID de playlist: {self.id_playlist}"
            f"Nombre de la playlist: {self.nombre}"
            f"Canciones de la playlist: {self.canciones}"
        )

    def añadir_cancion(self, cancion: Cancion):
        self.canciones.append(cancion)

    def eliminar_cancion(self, id: int):
        for cancion in self.canciones:
            if cancion.id == id:
                self.canciones.remove(cancion)

    def duracion_total(self):
        return 

    def buscar_por_artista(self, artista: str):
        resultado = []
        for cancion in self.canciones:
            if artista in cancion.artistas:
                resultado.append(cancion)
        return resultado

    def buscar_por_genero(self, genero: str):
        pass

    def cancion_mas_corta(self):
        return min()

    def cancion_mas_larga(self):
        return max()

    def ordenar_por_duracion(self):
        pass

    def año(self, año: int):
        pass

    def aleatorio(self):
        random.shuffle(self.canciones)