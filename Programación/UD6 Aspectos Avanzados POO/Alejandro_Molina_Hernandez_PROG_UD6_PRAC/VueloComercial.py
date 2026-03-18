from Vuelo import Vuelo
from datetime import datetime


class VueloComercial(Vuelo):
    def __init__(self, nombre: str, empresa: str, piloto: str, tripulacion: list[str], pasajeros: int, precio_billete: float, entretenimiento: list[str], clases_disponibles: list[str], tipo_carga: str):
        super().__init__(nombre, empresa, piloto, tripulacion, pasajeros)
        self.precio_billete = precio_billete
        self.entretenimiento = entretenimiento
        self.clases_disponibles = clases_disponibles
        self.tipo_carga = tipo_carga
    
    def añadir_entretenimiento(self, nuevo: str):
        self.entretenimiento.append(nuevo)
    

    def eliminar_entretenimiento(self, eliminar: int):
        self.entretenimiento.remove(eliminar)


    def cambiar_tipo(self, nueva_carga: str):
        self.tipo_carga = nueva_carga


    def __str__(self):
        base = super().__str__().replace("Vuelo", "Vuelo Comercial")
        return f"{base} -- {self.precio_billete} -- {self.entretenimiento} -- {self.tipo_carga}"