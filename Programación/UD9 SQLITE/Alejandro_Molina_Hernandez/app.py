from Banda import Banda
from Vinilo import Vinilo
from pathlib import Path
import sqlite3


ruta = Path(__file__).parent / "coleccion_vinilos.db"


def menu() -> str:
    return f"Menu\n ------\n [M]ostrar\n [A]ñadir albúm\n [S]alir"


def conectar() -> sqlite3.Connection:
    conexion = sqlite3.connect(ruta)
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


def obtener_vinilos(conexion: sqlite3.Connection) -> list[Vinilo]:
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre
        FROM vinilos
        ORDER BY id
    """)

    filas = cursor.fetchall()

    vinilos = []

    for id, nombre in filas:
        vinilos.append(Vinilo(id, nombre))

    return vinilos


def mostrar_vinilos(conexion: sqlite3.Connection):
    vinilos = obtener_vinilos(conexion)

    print("\nColeccion de Vinilos")
    print("--------------------")

    for vinilo in vinilos:
        print(vinilo)


def obtener_bandas(conexion: sqlite3.Connection) -> list[Banda]:
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre
        FROM grupos
        ORDER BY id
    """)

    filas = cursor.fetchall()

    bandas = []

    for id, nombre in filas:
        bandas.append(Banda(id, nombre))

    return bandas


def mostrar_bandas(conexion: sqlite3.Connection):
    bandas = obtener_bandas(conexion)

    print("\nBandas Disponibles")
    print("--------------------")

    for banda in bandas:
        print(banda)

def crear_album(conexion: sqlite3.Connection, opcion_album: str | int):
    nombre_album = input("Nombre del albúm: ").strip()
    opcion = opcion_album

    cursor = conexion.cursor()

    if opcion.lower() == "n":
        banda_usada = input("Nombre de la nueva banda: ")

        cursor.execute("""
        INSERT INTO grupos (nombre)
        VALUES (?)
        """, (banda_usada))
        conexion.commit()

        fila = banda_usada

    elif opcion.isdigit():
        banda_usada = opcion

        cursor.execute("""
        SELECT nombre from grupos
        WHERE id = ?
        """, (opcion))
        
        fila = cursor.fetchall()

    
    try:
        cursor.execute("""
            INSERT INTO vinilos (nombre, id_grupo)
            VALUES (?, ?)
        """, (nombre_album, fila))
        conexion.commit()
        print("Albúm añadido correctamente.")
    except sqlite3.IntegrityError as error:
        print(f"No se ha podido crear el albúm: {error}")


def main() -> None:
    conexion = None

    try:
        conexion = conectar()
    except sqlite3.Error as error:
        print(f"Ha habido un error al conectar con la base de datos: {error}")
        return
    
    while True:
        print("Menu\n------\n[M]ostrar\n[A]ñadir albúm\n[S]alir")
        opcion = input("Opción: ")

        if opcion.lower() == "s":
            print("Saliendo del programa.")
            break

        elif opcion.lower() == "m":
            mostrar_vinilos(conexion)

        elif opcion.lower() == "a":
            mostrar_bandas(conexion)
            opcion_album = input("Elige una banda por id o [N]ueva: ")

            crear_album(conexion, opcion_album)

    if conexion is not None:
        conexion.close()


if __name__ == "__main__":
    main()