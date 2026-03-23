from pathlib import Path


class Producto:
    def __init__(self, id: int, nombre: str, precio: float, stock: int):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def __str__(self):
        return f"{self.nombre} -- {self.precio}€ -- {self.stock}"

if __name__ == "__main__":

    productos = []

    archivo = Path(__file__).parent / "productos.csv"

    with open(archivo, "r", encoding="utf-8") as f:
        next(f)
        for linea in f:
            id, nombre, precio, stock = linea.strip().split(",")
            producto = Producto(int(id), nombre, precio, stock)
            productos.append(producto)

    for p in productos:
        print(p)