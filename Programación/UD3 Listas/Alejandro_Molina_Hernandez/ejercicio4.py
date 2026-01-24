mermeladas = []

while True:
    print("MENÚ")
    print("1) Ver mermeladas")
    print("2) Insertar mermeladas")
    print("0) Salir")
    opcion_elegida = int(input("Inserta un opcion: "))

    if opcion_elegida == 0:
        break

    if opcion_elegida == 1 and mermeladas:
        print(mermeladas)
    else:
        print("No hay mermeladas registradas.")

    if opcion_elegida == 2:
        nombre = input("Nombre de la mermelada : ")
        ingredientes = [input("Ingredientes(separados por coma): ")]
        azucar = int(input("Cantidad de azúcar: "))
        ecologica = input("Es ecológica? (S/N): ")

        ecologica_bool = False

        if ecologica == "S":
            ecologica_bool = True
        else:
            ecologica_bool = False

        nueva = []

        nueva.append(nombre)
        nueva.append(ingredientes)
        nueva.append(azucar)
        nueva.append(ecologica_bool)
        mermeladas.append(nueva)
    

        

    
