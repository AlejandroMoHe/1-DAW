from Vuelo import Vuelo

class VueloPrivado(Vuelo):

    COSTE_AVION = 5000

    def __init__(self, nombre: str, empresa: str, piloto: str, tripulacion: list[str], pasajeros: int, cliente: str, servicios: list[str]) -> None:
        super().__init__(nombre, empresa, piloto, tripulacion, pasajeros)
        self.cliente = cliente
        self.servicios = servicios

    def añadir_servicio(self, servicio: str) -> None:
        self.servicios.append(servicio)

    def eliminar_servicio(self, servicio: str) -> None:
        if servicio in self.servicios:
            self.servicios.remove(servicio)
    
    def calcular_coste(self) -> float:
        return self.COSTE_AVION + (len(self.servicios) * 200)
    
    def __str__(self):
        base = super().__str__().replace("Vuelo", "Vuelo Privado")
        return f"{base} -- {self.cliente} -- {self.servicios}"

if __name__ == "__main__":
    vp = VueloPrivado("VP1", "JetLux", "Mario", ["Laura"], 10, "Empresa X", ["wifi"])

    print("=== ESTADO INICIAL ===")
    print(vp)

    print("\n=== TRIPULANTE Y PILOTO ===")
    vp.agregar_tripulante("Sonia")
    vp.cambiar_piloto("Carlos")
    print(vp)

    print("\n=== SERVICIOS ===")
    vp.añadir_servicio("bar")
    vp.añadir_servicio("tv")
    vp.eliminar_servicio("wifi")
    print(vp)

    print("\n=== COSTE DEL VUELO ===")
    print(vp.calcular_coste())
