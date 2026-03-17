from Vuelo import Vuelo

class VueloPrivado(Vuelo):
    def __init__(self, nombre: str, empresa: str, piloto: str, tripulacion: list[str], pasajeros: int, cliente: str, servicios: list[str]):
        super().__init__(nombre, empresa, piloto, tripulacion, pasajeros)
        self.cliente = cliente
        self.servicios = servicios

    def __str__(self):
        base = super().__str__().replace("Vuelo", "Vuelo Privado")
        return f"{base} -- {self.cliente} -- {self.servicios}"