from pathlib import Path


archivo = Path(__file__).parent / "datos" / "pi.txt"

pi = 3

while True:
    print("Iteración 1 --> π ~ 3.0")
    print("Enter para la siguiente iteración o 's' para salir")
    opcion = input()

    if opcion.lower() == "s":
        print("Saliendo")
        break
    else:
        pass
