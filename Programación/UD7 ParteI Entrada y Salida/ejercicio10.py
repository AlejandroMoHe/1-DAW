from pathlib import Path
import json


class Producto:
    def __init__(self, id: int, nombre: str, precio: float, stock: int):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def __str__(self):
        return f"{self.nombre} -- {self.precio}€ -- {self.stock}"

if __name__ == "__main__":

    archivo = Path(__file__).parent / "productos.json"

    productos = []

    with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)

            for d in datos:
                producto = Producto(
                    d["id"],
                    d["nombre"],
                    d["precio"],
                    d["stock"]
                )
                productos.append(producto)
    
    for p in productos:
        print(p)