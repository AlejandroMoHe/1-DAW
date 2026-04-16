import json
from pathlib import Path


class Habitat:

    def __init__(self, tipo: str, zona: str, clima: str):
        self.tipo = tipo
        self.zona = zona
        self.clima = clima


class Dinosaurio:

    def __init__(self, nombre: str, periodo: str, habitat: Habitat):
        self.nombre = nombre
        self.periodo = periodo
        self.habitat = habitat


if __name__ == "__main__":

    ruta = Path(__file__).parent / "datos" / "dinos.json"

    dinosaurios = []

    with open(ruta, "r", encoding="utf-8") as f:
        datos = json.load(f)
        
        for d in datos:
            datos_habitat = d["habitat"]
            habitat = Habitat(
                datos_habitat["tipo"],
                datos_habitat["zona"],
                datos_habitat["clima"]
            )

            d = Dinosaurio(
                d["nombre"],
                d["periodo"],
                habitat
            )

            dinosaurios.append(d)