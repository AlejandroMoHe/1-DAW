from Producto import Producto
from datetime import datetime

def productos_caros(productos: list[Producto], precio_min: float) -> list[Producto]:
    return [p.id for p in productos if p.precio >= precio_min]


def productos_de_categoria(productos: list[Producto], categoria: str) -> list[Producto]:
    return [p.id for p in productos if categoria in p.categorias]


def productos_multicategoria(productos: list[Producto]) -> list[Producto]:
    return [p.id for p in productos if len(p.categorias) > 1]


def productos_caducados(productos: list[Producto]) -> list[Producto]:
    return [p.id for p in productos if p.fecha_caducidad < datetime.now()]


def producto_mas_caro(productos: list[Producto]) -> Producto | None:
    mas_caro = max(productos, key= lambda p: p.precio)
    return mas_caro.id


def ordenar_por_caducidad(productos: list[Producto]) -> list[Producto]:
    return sorted(productos, key=lambda p: p.fecha_caducidad)


def hay_productos_caducados(productos: list[Producto]) -> bool:
    for p in productos:
        if p.fecha_caducidad > datetime.now():
            return True
        else:
            return False


def eliminar_caducados(productos: list[Producto]) -> list[Producto]:
    eliminar = []
    for p in productos:
        if p.fecha_caducidad > datetime.now():
            eliminar.append(p.id)
    return eliminar


def dias_en_super(productos: list[Producto]) -> dict[int, int]:
    cuenta = {}
    for p in productos:
        cuenta[p] = cuenta.get(p, 0) + 1
    return cuenta

def conteo_por_categoria(productos: list[Producto]) -> dict[str, int]:
    pass


if __name__ == "__main__":
    from datos import get_productos

    productos = get_productos()

    print("=== PRODUCTOS CAROS (>= 2.0€) ===")
    print(productos_caros(productos, 2.0))
    print()

    print("=== PRODUCTOS DE CATEGORÍA 'Lácteos' ===")
    print(productos_de_categoria(productos, 'Lácteos'))
    print()

    print("=== PRODUCTOS MULTICATEGORÍA ===")
    print(productos_multicategoria(productos))
    print()

    print("=== PRODUCTOS CADUCADOS ===")
    print(productos_caducados(productos))
    print()

    print("=== PRODUCTOS MÁS CAROS ===")
    print(producto_mas_caro(productos))
    print()

    print("=== ORDENADOS POR CADUCIDAD ===")
    id_ordenados = []
    for p in ordenar_por_caducidad(productos):
        id_ordenados.append(p.id)
    print(id_ordenados)
    print()
    
    print("=== ¿HAY PRODUCTOS CADUCADOS? ===")
    print(hay_productos_caducados(productos))
    print()

    print("=== ELIMINAR CADUCADOS ===")
    print(eliminar_caducados(productos))
    print()

    print("=== DIAS EN EL SUPERMERCADO ===")
    print(dias_en_super(productos))
    print()

    print("=== CONTEO POR CATEGORÍA ===")
    print(conteo_por_categoria(productos))