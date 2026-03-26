from pathlib import Path
import json


class Personaje:
    def __init__(self, nombre: str, posiciones: list[str], dificultad: str):
        self.nombre = nombre
        self.posiciones = posiciones
        self.dificultad = dificultad
    
    def __str__(self):
        return f"{self.nombre} -- {self.posiciones} -- {self.dificultad}"

if __name__ == "__main__":

    archivo = Path(__file__).parent / "lol.json"

    personajes = []

    with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)

            for d in datos:
                personaje = Personaje(
                    d["nombre"],
                    d["posiciones"],
                    d["dificultad"]
                )
                if "Top" in personaje.posiciones and personaje.dificultad == "Baja":
                    personajes.append(personaje)
    
    for p in personajes:
        print(p)