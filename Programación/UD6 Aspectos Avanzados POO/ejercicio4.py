class Suscripcion:
    
    COMISION = 0.16
    
    def __init__(self, nombre: str, precio_base: float) -> None:
        self.nombre = nombre
        self.precio_base = precio_base

    def precio_final(self) -> float:
        return self.precio_base * (1 + Suscripcion.COMISION)

if __name__ == "__main__":
    suscripcion1 = Suscripcion("Netflix", 23.50)
    suscripcion2 = Suscripcion("Amazon Prime", 10.20)

    print(suscripcion1.precio_final())
    print(suscripcion2.precio_final())