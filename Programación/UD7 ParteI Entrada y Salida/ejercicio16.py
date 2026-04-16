from pathlib import Path

config = Path(__file__).parent / "datos" / "configuracion.txt"

if config == False:
    with open(config, "w", encoding="utf-8") as f:
        f.write("Contador=0")


with open(config, "r", encoding="utf-8") as f:
    for linea in f:
        separados = linea.split("=")
        contador = int(separados[1])

while True:
    print(f"Contador: {contador}")
    tecla = input("Pulsa una tecla --> ")
    if tecla.lower() != "s":
        contador += 1
        with open(config, "w", encoding="utf-8") as f:
            f.write(f"Contador={contador}")
    else:
        with open(config, "w", encoding="utf-8") as f:
            f.write(f"Contador={contador+1}")
        break