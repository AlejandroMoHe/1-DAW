from Vuelo import Vuelo


class VueloComercial(Vuelo):
    def __init__(self, nombre: str, empresa: str, piloto: str, tripulacion: list[str], pasajeros: int, destino: str, tipo_carga: str):
        super().__init__(nombre, empresa, piloto, tripulacion, pasajeros)
        self.destino = destino
        self.tipo_carga = tipo_carga
    
    def __str__(self):
        base = super().__str__().replace("Vuelo", "Vuelo Comercial")
        return f"{base} -- {self.destino} -- {self.tipo_carga}"