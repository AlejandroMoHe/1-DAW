while True:
    print("MENÚ DE CÁLCULOS FÍSICOS")
    print("1. Fuerza = masa * aceleración")
    print("2. Velocidad = espacio / tiempo")
    print("3. Presión = fuerza / superficie")
    print("4. Densidad = masa / volumen")
    print("5. Salir")

    opcion = int(input("Elige una opcion (1-5): "))

    if opcion == 5:
        break

    if opcion == 1:
        masa = int(input("Introduce la masa (kg): "))
        aceleracion = int(input("Introduce la aceleracion (m/s²): "))
        fuerza = masa * aceleracion
        print(f"La fuerza es de {fuerza} N")

    elif opcion == 2:
        espacio = int(input("Introduce el espacio(m): "))
        tiempo = int(input("Introduce el tiempo(s): "))
        velocidad = espacio / tiempo
        print(f"La velocidad es de {velocidad} m/s")

    elif opcion == 3:
        fuerza = int(input("Introduce la fuerza: "))
        superficie = int(input("Introduce la superficie: "))
        presion = fuerza / superficie
        print(f"La presion es de {presion} Pa")

    elif opcion == 4:
        masa = int(input("Introduce la masa (kg): "))
        volumen = int(input("Introduce el volumen: "))
        densidad = masa / volumen
        print(f"La densidad es de {densidad} kg/m³")
print("Fin del programa")