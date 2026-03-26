from pathlib import Path
import json


class Persona:
    def __init__(self, id: int, nombre: str, campo: str, aportacion: dict):
        self.id = id
        self.nombre = nombre
        self.campo = campo
        self.aportacion = aportacion
    
    def __str__(self):
        return f"ID {self.id} -- Nombre: {self.nombre} -- Campo: {self.campo} -- Aportación: {self.aportacion}"

class Aportacion:
     def __init__(self, nombre: str, anio: str, importancia: dict):
        self.id = id
        self.nombre = nombre
        self.anio = anio
        self.importancia = importancia

if __name__ == "__main__":

    archivo = Path(__file__).parent / "gente-lista.json"

    personas = []

    with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)

            for d in datos:
                persona = Persona(
                    d["id"],
                    d["nombre"],
                    d["campo"],
                    d["aportacion"]
                )
                personas.append(persona)
            
            datos = json.load(f)

            for d in datos:
                persona = Persona(
                    d["id"],
                    d["nombre"],
                    d["campo"],
                    d["aportacion"]
                )
                personas.append(persona)
    
    for p in personas:
        print(p)