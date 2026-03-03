from datetime import datetime


class Mascota:
    def __init__(self, id: int, nombre: str, tipo: str, fecha_entrada: datetime, precio: float, fecha_nacimiento: datetime, fecha_venta: datetime | None, vacunas: list[str] | None) -> None:
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.fecha_entrada = fecha_entrada
        self.precio = precio
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_venta = fecha_venta
        self.vacunas = vacunas
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Mascota):
            return False
        return self.id == other.id
    

    def se_vacuna(self) -> bool:
        return self.vacunas != None


    def edad(self) -> int:
        hoy = datetime.today()
        edad = self.fecha_nacimiento - hoy
        return edad


    def __str__(self) -> str:
        return f"{self.tipo} - {self.fecha_nacimiento} - {self.precio}€ [{self.id}]"
    

if __name__ == "__main__":
    from datetime import date, timedelta

    hoy = date.today()

    mascota1 = Mascota(1, "Misu", "Gato", hoy - timedelta(days=10), 120.0, hoy - timedelta(days=365*2), None, ["Rabia", "Trivalente"])

    mascota2 = Mascota(2, "Venom", "Tarantúla", hoy - timedelta(days=3), 45.5, hoy - timedelta(days=365), None, None)

    print("=== PRUEBAS DE MASCOTA ===")
    print()
    print("Pruebas para el gato")
    print(mascota1)
    print(f"¿Se vacuna gato? {mascota1.se_vacuna()}")
    print()
    print("Pruebas para la araña")
    print(mascota2)
    print(f"¿Se vacuna gato? {mascota2.se_vacuna()}")
    print()
    print(f"¿Es el gato igual a la araña? {mascota1==mascota2}")
    print(f"¿Es la araña igual a ella misma? {mascota2==mascota2}")
