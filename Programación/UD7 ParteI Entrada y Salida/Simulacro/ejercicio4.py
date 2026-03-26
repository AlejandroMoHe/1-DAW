from pathlib import Path
from random import randint


configuracion = Path(__file__).parent / "datos" / "config.txt"
dado = ""
tiradas = 0

while True:
    with open(configuracion, "r", encoding="utf-8") as f:
    
        for linea in f:
            separados = linea.split("=")
            if separados[0] == "tipo_dado":
                dado = separados[1]
            elif separados[0] == "num_tiradas":
                tiradas = separados[1]
    
    print(
        "1. Simular\n"
        "2. Configurar\n"
        "0. Salir\n"
    )
    opcion = int(input("Elige una opción: "))

    if opcion == 0:
        print("Saliendo del programa...")
        break
    
    elif opcion == 1:
        with open("simulacion.txt", "w", encoding="utf-8") as f:
                tiradas_simula = int(tiradas)
                for _ in range(tiradas_simula):
                    num = randint(1, tiradas_simula)
                    f.write(f"{num}\n")
        print("Simulación realizada correctamente.")
    
    elif opcion == 2:
        print(f"Configuración actual:{dado}, {tiradas}tiradas")
        config_opcion = input("¿Quieres cambiar la configuración? (S/N): ")
        if config_opcion == "S":
            nuevo_dado = input("Nuevo tipo de dado: ")
            nueva_tirada = int(input("Nuevo número de tiradas: "))
            with open(configuracion, "w", encoding="utf-8") as f:
                f.write(f"tipo_dado={nuevo_dado}\nnum_tiradas={nueva_tirada}")
            print("Configuración guardada correctamente.")