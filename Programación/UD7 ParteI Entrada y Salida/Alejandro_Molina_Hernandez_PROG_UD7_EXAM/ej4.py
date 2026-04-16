from pathlib import Path
import random


def leer_config(ruta: Path) -> tuple[str, int]:
    inicio = 0
    fin = 1
    cantidad = 0
    salida = ""
    primos = ""

    with open(ruta, "r", encoding="utf-8") as f:

        for linea in f:
            linea = linea.strip()
            if linea:
                partes = linea.split(":")
                clave = partes[0]
                valor = partes[1]

                if clave == "inicio":
                    inicio = int(valor)
                elif clave == "fin":
                    fin = int(valor)
                if clave == "cantidad":
                    cantidad = int(valor)
                elif clave == "salida":
                    salida = valor
                if clave == "solo_primos":
                    primos = valor

    return inicio, fin, cantidad, salida, primos


def guardar_config(ruta: Path, inicio: str, fin: int, cantidad: int, salida: str, primos: str) -> None:
    with open(ruta, "w", encoding="utf-8") as f:

        f.write(f"inicio:{inicio}\n")
        f.write(f"fin:{fin}\n")
        f.write(f"cantidad:{cantidad}\n")
        f.write(f"salida:{salida}\n")
        f.write(f"solo_primos:{primos}")


def crear_numero(ruta: Path, inicio: int, fin: int, cantidad: int, primos: str) -> None:
    with open(ruta, "w", encoding="utf-8") as f:
        
        for i in range(cantidad):
            num = random.randint(inicio, fin)
            if primos == "true":
                if es_primo(num, 2):
                    f.write(f"{num}\n")
            else:
                f.write(f"{num}\n")


def es_primo(n: int, d: int = 2) -> bool:
    return False if n < 2 else True if d * d > n else False if n % d == 0 else es_primo(n, d + 1)


if __name__ == "__main__":

    ruta_config = Path(__file__).parent / "ej4-config.txt"
    ruta_resultados = Path(__file__).parent / "ejercicio4-resultado.txt"


    inicio, fin, cantidad, salida, primos = leer_config(ruta_config)

    while True:
        print("--- MENÚ ---")
        print("\n1. Calcular")
        print("2. Configurar")
        print("3. Salir")
        opcion = int(input("Elige opción: "))

        if opcion == 1:
            if salida == "fichero":
                crear_numero(ruta_resultados, inicio, fin, cantidad, primos)
                print("Resultados guardados en fichero.")
            else:
                print("Resultados: ")
                numeros = []

                for _ in range(cantidad):
                    num = random.randint(inicio, fin)
                    if primos == "true":
                        if es_primo(num, 2):
                            numeros.append(num)
                        else:
                            numeros.append(num)
                
                print(numeros)

        elif opcion == 2:
            print(f"--- CONFIGURACIÓN ACTUAL ---")
            print(f"inicio: {inicio}")
            print(f"fin: {fin}")
            print(f"cantidad {cantidad}")
            print(f"salida: {salida}")
            print(f"solo_primos: {primos}")
            respuesta = input("¿Quieres cambiar la configuración? (s/n): ")

            if respuesta.lower() == "s":
                print("--- EDITAR CONFIGURACIÓN ---")
                print(f"Inicio ({inicio}): ")
                inicio = int(input(""))
                print(f"Fin ({fin}): ")
                fin = int(input(""))
                print(f"Cantidad ({cantidad}): ")
                cantidad = int(input(""))
                print(f"Salida [pantalla/fichero] ({salida}): ")
                salida = input("")
                print(f"Solo primos [true/false] ({primos}): ")
                primos = input("")

                guardar_config(ruta_config, inicio, fin, cantidad, salida, primos)
                print("Configuración guardada.")
            else:
                print("Configuración no modificada.")

        elif opcion == 3:
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida.")