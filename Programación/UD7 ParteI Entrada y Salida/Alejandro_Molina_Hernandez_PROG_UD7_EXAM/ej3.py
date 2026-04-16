from pathlib import Path


if __name__ == "__main__":

    carpeta_script = Path(__file__).parent

    ruta = Path(__file__).parent / "datos" / "divina-comedia.txt"
    ruta_resultados = Path(__file__).parent / "ej3-resultado.txt"

    lineas = []
    linea_mas_larga = ""
    max_longitud = 0
    linea_mas_m = ""
    num_m = 0
    max_m = 0

    with open(ruta, "r", encoding="utf-8") as f:

        for linea in f:

            longitud = len(linea)
            if longitud > max_longitud:
                max_longitud = longitud
                linea_mas_larga = linea
            
            for letra in linea:
                num_m = linea.lower().count("m")
                if num_m > max_m:
                    max_m = num_m
                    linea_mas_m = linea

    with open(ruta_resultados, "w", encoding="utf-8") as f:
        f.write(f"### APARTADO A:\n")
        f.write(f"### APARTADO B:\n {linea_mas_larga}\n")
        f.write(f"### APARTADO C:\n {linea_mas_m}\n")