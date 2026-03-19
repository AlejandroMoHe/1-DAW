import random
from pathlib import Path


def leer_configuracion(nombre_archivo: str) -> dict:
    config = {}

    with open(nombre_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            clave, valor = linea.strip().split("=")
            config[clave] = valor

    return config

def jugar(config: dict):

    tablas = int(config["tablas"])
    problemas = int(config["preguntas"])

    for _ in range(1, problemas):
        num1 = random.randint(tablas)
        num2 = random.randint(0, 9)
        respuesta = int(input(f"{num1} x {num2} = ? "))
        resultado = num1 * num2
        if respuesta == resultado:
            print("Correcto")
        else:
            print(f"Incorrecto. La respuesta es {resultado}")

if __name__ == "__main__":
    nombre_archivo = Path(__file__).parent / "config7.txt"
    config = leer_configuracion(nombre_archivo)
    jugar(config)


