import random

def elegirPalabra(lista: list) -> str:
    palabraElegida = random.randint(0, len(lista) - 1)
    return lista[palabraElegida]

def crearOculta(palabra: str) -> list:
    palabraOculta = []
    for _ in palabra:
        palabraOculta.append("_")
    return palabraOculta

def mostrarEstado(vidas: int, palabraOculta: list):
    print(f"Tienes {vidas} vidas")
    print("Palabra que debes encontrar: ")
    print(palabraOculta)

def comprobarLetra(letra: str, palabra: str, palabraOculta: list, usadas: list) -> int:
    if letra in usadas:
        return -1

    usadas.append(letra)
    acierto = False

    for i in range(len(palabra)):
        if palabra[i] == letra:
            palabraOculta[i] = letra
            acierto = True

    if acierto:
        return 1
    else:
        return -1

def palabraResuelta(palabraOculta: list) -> bool:
    for letra in palabraOculta:
        if letra == "_":
            return False
    return True
