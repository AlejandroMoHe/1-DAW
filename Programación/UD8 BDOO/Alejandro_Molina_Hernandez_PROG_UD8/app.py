from ZODB import DB
from ZODB.FileStorage import FileStorage
import transaction
from persistent import Persistent
from persistent.list import PersistentList
from pathlib import Path
import random


class Frase(Persistent):

    def __init__(self, frase: str, autor: str):
        self.frase = frase
        self.autor = autor

    def __str__(self):
        return f"{self.frase} - {self.autor}"


def mostrar_menu():
    print("\n[S]iguiente - [M]odificar - [B]orrar - [N]ueva frase")


def modificar_frase(frase):

    print("\n--- Modificar frase ---")

    nueva_frase = input(f"Nueva frase[{frase.frase}]: ")
    nuevo_autor = input(f"Nuevo autor[{frase.autor}]: ")

    frase.frase = nueva_frase
    frase.autor = nuevo_autor

    transaction.commit()

    print("\nFrase modificada correctamente.")


def borrar_frase(frase_actual, items):

    items.remove(frase_actual)

    transaction.commit()

    print("\nFrase borrada correctamente.")

    if len(items) > 0:
        return random.choice(items)

    return None


def nueva_frase(items):

    frase = input("Frase: ")
    autor = input("Autor: ")

    nueva = Frase(frase, autor)

    items.append(nueva)

    transaction.commit()

    print("\nFrase añadida correctamente.")

    return nueva

carpeta = Path(__file__).resolve().parent
storage = FileStorage(str(carpeta / "checklist.fs"))
db = DB(storage)
connection = db.open()
root = connection.root()

if "items" not in root or len(root["items"]) == 0:

    root["items"] = PersistentList([
        Frase("Estoy a 2 pensamientos raros de convertirme en NPC.", "Cualquier persona"),
        Frase("El éxito me persigue, pero yo soy más rápido.", "Usain Bolt"),
        Frase("Si funciona, fue intencional; si no, también.", "Albert Einstein"),
        Frase("El backend llora, el frontend disimula.", "Jefe de la empresa"),
        Frase("Si busca resultados distintos, no hagas siempre lo mismo.", "Albert Einstein"),
        Frase("No es un error, es una versión alternativa.", "Albert Einstein"),
        Frase("Commit: arreglos varios (no sé cuáles).", "Alumno de DAW"),
        Frase("Todo era null… como mis esperanzas.", "Becario")
    ])

    transaction.commit()

items = root["items"]

frase_actual = random.choice(items)

try:

    while True:

        print(f"\n{frase_actual}")

        mostrar_menu()

        opcion = input("Opción: ").lower().strip()

        if opcion == "s":

            frase_actual = random.choice(items)

        elif opcion == "m":

            modificar_frase(frase_actual)

        elif opcion == "b":

            frase_actual = borrar_frase(frase_actual, items)

            if frase_actual is None:

                print("\nNo quedan frases.")

                root["items"] = PersistentList([
                    Frase("Estoy a 2 pensamientos raros de convertirme en NPC.", "Cualquier persona"),
                    Frase("El éxito me persigue, pero yo soy más rápido.", "Usain Bolt"),
                    Frase("Si funciona, fue intencional; si no, también.", "Albert Einstein"),
                    Frase("El backend llora, el frontend disimula.", "Jefe de la empresa"),
                    Frase("Si busca resultados distintos, no hagas siempre lo mismo.", "Albert Einstein"),
                    Frase("No es un error, es una versión alternativa.", "Albert Einstein"),
                    Frase("Commit: arreglos varios (no sé cuáles).", "Alumno de DAW"),
                    Frase("Todo era null… como mis esperanzas.", "Becario")
                ])

                transaction.commit()

                items = root["items"]
                frase_actual = random.choice(items)

        elif opcion == "n":

            frase_actual = nueva_frase(items)

        else:
            print("\nOpción no válida.")

finally:
    connection.close()
    db.close()
    storage.close()