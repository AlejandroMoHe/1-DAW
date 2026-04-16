from pathlib import Path


class Elemento:
    def __init__(self, nombre:str, simbolo:str, num_atomico:int, masa_atomica:float, grupo:int):
        self.nombre= nombre
        self.simbolo = simbolo
        self.num_atomico = num_atomico
        self.masa_atomica = masa_atomica
        self.grupo = grupo

ruta = Path(__file__).parent / "datos" /"elementos.csv"


with open(ruta, "r", encoding="utf-8") as f:
    next(f)

    grupo1 = []
    resto = []
    
    for linea in f:
        nombre, simbolo, num_atomico, masa_atomica, grupo = linea.strip().split(",")
        elemento = Elemento(nombre, simbolo, int(num_atomico), float(masa_atomica), int(grupo))

        if elemento.grupo == 1:
            grupo1.append(elemento)
        else:
            resto.append(elemento)

if __name__ == "__main__":
    total = 0
    print("Elementos del grupo 1:")
    for e in grupo1:
        print(e.nombre)
    
    for e in grupo1:
        total += e.masa_atomica
        media1 = total / len(grupo1)
    
    for e in resto:
        total += e.masa_atomica
        media_resto = total / len(resto)


    print(f"\nMedia grupo 1: {media1:.2f}")
    print(f"Media resto: {media_resto:.2f}")
