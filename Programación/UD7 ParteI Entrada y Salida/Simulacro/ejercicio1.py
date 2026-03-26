from pathlib import Path
from datetime import datetime


class Planta:
    def __init__(self, id: int, producto: str, fecha: str, precio: float):
        self.id = id
        self.producto = producto
        self.fecha = fecha
        self.precio = precio
    
    def __str__(self):
        return f"{self.id} - {self.producto} - {self.fecha} - {self.precio}€"

if __name__ == "__main__":

    plantas = []
    total = 0

    archivo = Path(__file__).parent / "vivero.csv"

    with open(archivo, "r", encoding="utf-8") as f:
        next(f)
        for linea in f:
            id, producto, fecha, precio = linea.strip().split(",")
            planta = Planta(int(id), producto, fecha, float(precio))
            fecha_separada = fecha.split("/")
            fecha = datetime(int(fecha_separada[2]), int(fecha_separada[1]), int(fecha_separada[0]))

            if fecha.month == 1 and fecha.year == 2022:
                plantas.append(planta)
                total += planta.precio

    print("Ventas de enero 2022:")
    for p in plantas:
        print(p)

    print(f"Importe total: {round(total, 2)}€")
    print(f"Producto más caro: ")
    print(f"Precio Medio: ")
    
    