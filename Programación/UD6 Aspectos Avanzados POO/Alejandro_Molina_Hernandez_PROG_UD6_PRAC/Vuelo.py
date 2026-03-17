class Vuelo:

    EQUIPAJE_MAXIMO = 23.0

    def __init__(self, nombre: str, empresa: str, piloto: str, tripulacion: list[str], pasajeros: int):
        self.nombre = nombre
        self.empresa = empresa
        self.piloto = piloto
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros
    

    def __eq__(self, other):
        if isinstance(other, Vuelo):
            return self.nombre == other.nombre
        return False
    

    def __hash__(self):
        return hash(self.nombre)
    

    def agregar_tripulante(self, tripulante: str) -> bool:

        if tripulante in self.tripulacion:
            return False
        else:
            self.tripulacion.append(tripulante)
            return True

    def quitar_tripulante(self, tripulante: str) -> bool:

        if tripulante in self.tripulacion:
            self.tripulacion.remove(tripulante)
            return True
        else:
            return False
    

    def cambiar_piloto(self, nuevo_piloto: str) -> bool:
        if self.piloto == nuevo_piloto:
            return False
        else:
            self.piloto = nuevo_piloto
            return True


    def __str__(self):
        return f"Vuelo {self.nombre} -- {self.empresa} -- {self.piloto} -- {self.tripulacion} -- {self.pasajeros}"
    