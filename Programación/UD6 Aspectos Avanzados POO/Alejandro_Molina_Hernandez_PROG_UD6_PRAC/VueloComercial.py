from Vuelo import Vuelo


class VueloComercial(Vuelo):
    def __init__(self, nombre: str, empresa: str, piloto: str, tripulacion: list[str], pasajeros: int, precio_billete: float, entretenimiento: list[str], clases_disponibles: list[str], tipo_carga: str):
        super().__init__(nombre, empresa, piloto, tripulacion, pasajeros)
        self.precio_billete = precio_billete
        self.entretenimiento = entretenimiento
        self.clases_disponibles = clases_disponibles
        self.tipo_carga = tipo_carga
    
    def añadir_entretenimiento(self, nuevo: str) -> None:
        self.entretenimiento.append(nuevo)
    

    def eliminar_entretenimiento(self, eliminar: int) -> None:
        self.entretenimiento.remove(eliminar)


    def cambiar_carga(self, nueva_carga: str) -> None:
        self.tipo_carga = nueva_carga

    def calcular_coste(self) -> float:
        return self.pasajeros * self.precio_billete

    def __str__(self):
        base = super().__str__().replace("Vuelo", "Vuelo Comercial")
        return f"{base} -- {self.precio_billete} -- {self.entretenimiento} -- {self.tipo_carga}"
    
if __name__ == "__main__":
    vc = VueloComercial("VC1", "Ryanair", "Luis", ["Ana"], 180, 50.0, ["películas"], ["turista"], "equipaje")

    print("=== ESTADO INICIAL ===")
    print(vc)

    print("\n--- TRIPULANTE Y PILOTO ---")
    vc.agregar_tripulante("Carlos")
    vc.cambiar_piloto("Pedro")
    print(vc)

    print("\n--- ENTRETENIMIENTO Y CARGA ---")
    vc.añadir_entretenimiento("música")
    vc.cambiar_carga("mercancía")
    print(vc)

    print("\n--- Coste del vuelo ---")
    print(vc.calcular_coste())

