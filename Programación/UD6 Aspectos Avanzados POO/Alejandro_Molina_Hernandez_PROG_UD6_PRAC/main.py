from VueloComercial import VueloComercial
from VueloPrivado import VueloPrivado

vuelos_comerciales = [
    VueloComercial("VC1", "Ryanair", "Luis", ["Ana"], 180, 50.0, ["películas"], ["turista"], "equipaje"),
    VueloComercial("VC2", "Vueling", "Pedro", ["Marta"], 150, 60.0, ["música"], ["business"], "mercancía")
    ]
vuelos_privados = [
    VueloPrivado("VP1", "JetLux", "Mario", ["Laura"], 10, "Empresa X", ["wifi"]),
    VueloPrivado("VP2", "SkyVIP", "Carlos", ["Sonia"], 8, "Cliente Y", ["bar", "tv"])
]

while True:
    print("\n=== MENÚ ===")
    print("1. Vuelos comerciales")
    print("2. Vuelos privados")
    print("3. Añadir vuelo comercial")
    print("4. Añadir vuelo privado")
    print("5. Mostrar coste de todos los vuelos")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        for v in vuelos_comerciales:
            print(v)

    elif opcion == "2":
        for v in vuelos_privados:
            print(v)

    elif opcion == "3":
        nombre = input("Nombre: ")
        empresa = input("Empresa: ")
        piloto = input("Piloto: ")
        pasajeros = int(input("Pasajeros: "))
        precio = float(input("Precio billete: "))

        nuevo = VueloComercial(nombre, empresa, piloto, [], pasajeros, precio, [], [], "equipaje")
        vuelos_comerciales.append(nuevo)

    elif opcion == "4":
        nombre = input("Nombre: ")
        empresa = input("Empresa: ")
        piloto = input("Piloto: ")
        pasajeros = int(input("Pasajeros: "))
        cliente = input("Cliente: ")

        nuevo = VueloPrivado(nombre, empresa, piloto, [], pasajeros, cliente, [])
        vuelos_privados.append(nuevo)

    elif opcion == "5":
        print("\n=== COSTES DE LOS VUELOS ===")
        for v in vuelos_comerciales + vuelos_privados:
            print(f"{v.nombre}: {v.calcular_coste()}€")

    elif opcion == "0":
        print("Saliendo del programa")
        break

    else:
        print("Opción no válida")