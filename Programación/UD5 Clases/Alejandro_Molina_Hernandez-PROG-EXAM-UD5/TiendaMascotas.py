from Mascota import Mascota


class TiendaMascotas:
    def __init__(self, id: int, nombre: str, direccion: str, mascotas: list[Mascota]):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.mascotas = mascotas


    def añadir_mascota(self, mascota: Mascota) -> None:
        self.mascotas.append(mascota)
        id_disponibles = []
        for m in self.mascotas:
            id_disponibles.append(m.id)
        return id_disponibles


    def eliminar_mascota(self, id: int) -> bool:
        for m in self.mascotas:
            if m.id == id:
                self.mascotas.remove(m)
                return True
        return False
    

    def mascotas_rango_precio(self, a: float, b: float) -> list[Mascota]:
        mascotas_en_rango = []
        for m in self.mascotas:
            if m.precio >= a and m.precio <= b:
                mascotas_en_rango.append(m.id)
        return mascotas_en_rango

    
    def no_necesitan_vacunas(self) -> list[Mascota]:
        no_vacunar = []
        for m in self.mascotas:
            if m.vacunas == None:
                no_vacunar.append(m.id)
        return no_vacunar

    def mas_antiguas(self) -> list[Mascota]:
        return sorted(self.mascotas, key=lambda p: p.fecha_entrada)


    def mascotas_por_tipo(self, tipo: str) -> list[Mascota]:
        mismo_tipo = []
        for m in self.mascotas:
            if tipo == m.tipo:
                mismo_tipo.append(m.id)
        return mismo_tipo
    

    def mascotas_por_tipos(self, tipos: list[str]) -> list[Mascota]:
        mismos_tipos = []
        for m in self.mascotas:
            if tipos in m.tipo:
                mismos_tipos.append(m.id)
        return mismos_tipos
    

    def actualizar_precio_por_tipo(self, tipo: str, porcentaje: float) -> None:
        pass


    def reporte_por_tipo(self) -> dict[str, dict[str, float]]:
        pass


if __name__ == "__main__":

    from datos import get_datos
    from datetime import timedelta, date

    hoy = hoy = date.today()
    datos = get_datos()
    tienda = TiendaMascotas(1, "Tienda", "Avenida de Andalucía 45, 18014 Granada", datos)

    mascota1 = Mascota(99, "A", "Tortuga", hoy - timedelta(days=10), 200.0, hoy - timedelta(days=800), None, None)

    print("=== DISPONIBLES ===")
    for mascota in tienda.mascotas:
        if mascota.fecha_venta == None:
            print(mascota)
    print()
    print("=== VENDIDAS ===")
    for mascota in tienda.mascotas:
        if mascota.fecha_venta != None:
            print(mascota)
    print()
    print("=== MASCOTAS EN RANGO DE PRECIO (100 - 200) ===")
    print(tienda.mascotas_rango_precio(100, 200))
    print()
    print("=== NO NECESITAN VACUNAS ===")
    print(tienda.no_necesitan_vacunas())
    print()
    print("=== MÁS ANTIGÜAS (ordenadas por fecha de entrada) ===")
    id_ordenados = []
    for p in tienda.mas_antiguas():
        id_ordenados.append(p.id)
    print(id_ordenados)
    print()
    print("=== MASCOTAS POR TIPO 'Gato' ===")
    print(tienda.mascotas_por_tipo('Gato'))
    print()
    print("=== MASCOTAS POR TIPOS ['Gato', 'Erizo'] ===")
    print(tienda.mascotas_por_tipo(['Gato', 'Erizo']))
    print()
    print("=== ACTUALIZAR PRECIO +10% A LOS GATOS ===")
    print()
    print()
    print("=== REPORTE POR TIPO (VENDIDAS) ===")
    print()
    print()
    print("=== ELIMINAR MASCOTA ID 3 ===")
    print(f"Eliminada: {tienda.eliminar_mascota(3)}")
    print()
    print("=== AÑADIR NUEVA MASCOTA ===")
    print(tienda.añadir_mascota(mascota1))
    print()