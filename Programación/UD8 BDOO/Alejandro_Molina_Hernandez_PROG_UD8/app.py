from ZODB import DB
from ZODB.FileStorage import FileStorage
import transaction
from persistent import Persistent
from persistent.list import PersistentList
import random


class Frase(Persistent):
    def __init__(self, frase: str, autor: str):
        self.frase = frase
        self.autor = autor

    
    def __str__(self):
        return f"{self.frase} - {self.autor}\n"
    

storage = FileStorage("./checklist.fs")
db = DB(storage)
connection = db.open()
root = connection.root()

if "items" not in root:
    root["items"] = PersistentList()

items = root["items"]

frases = [Frase("Estoy a 2 pensamientos raros de convertirme en NPC.", "Cualquier persona"),
          Frase("El éxito me persigue, pero yo soy más rápido.", ""),
          Frase("Si funciona, fue intencional; si no, también.", ""),
          Frase("El backend llora, el frontend disimula.", ""),
          Frase("Si busca resultados distintos, no hagas siempre lo mismo.", "Albert Einstein"),
          Frase("No es un error, es una versión alternativa.", ""),
          Frase("Commit: arreglos varios (no sé cuáles).", ""),
          Frase("Todo era null… como mis esperanzas.", "")
          ]

frase = random.choice(frases)


while True:
    
    print(f"{frase}\n")
    print("[S]iguiente - [M]odificar - [B]orrar - [N]ueva frase")

    opcion = input("Opción: ")

    if opcion.lower() == "s":
        frase = random.choice(frases)
    
    elif opcion.lower() == "m":
        pass

    elif opcion.lower() == "b":
        pass

    elif opcion.lower() == "n":
        pass


    connection.close()
    db.close()
    storage.close()