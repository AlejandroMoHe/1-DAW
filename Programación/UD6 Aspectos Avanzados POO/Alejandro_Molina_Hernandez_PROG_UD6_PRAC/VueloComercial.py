from Vuelo import Vuelo


class VueloComercial(Vuelo):
    def __init__(self, nombre: str, empresa: str, piloto: str, tripulacion: list[str], pasajeros: int, ):
        super().__init__(nombre, empresa, piloto, tripulacion, pasajeros)