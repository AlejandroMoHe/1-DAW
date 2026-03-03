from BibliotecaEstudios import BibliotecaEstudios
from datos import get_datos
from EstudiosAnima import Estudio
from datetime import date

biblioteca = BibliotecaEstudios(1, "Biblioteca Animación", get_datos(0))

def mostrar_estudios():
    print("\n===== LISTADO DE ESTUDIOS =====")
    for e in biblioteca.estudios:
        print(f"{e.id} | {e.nombre} | {e.ganancias} millones (€)")

while True:
    mostrar_estudios()

    print("\n===== MENÚ PRINCIPAL =====")
    print("Introduce un ID positivo para ver detalles")
    print("Introduce un ID negativo para eliminar")
    print("[O] Ordenar")
    print("[A] Añadir")
    print("[S] Salir")

    opcion = input("Opción: ")

    if opcion.lower() == "s":
        print("Saliendo del programa...")
        break

    elif opcion.lower() == "o":
        print("\n--- ORDENAR POR ---")
        print("1. Nombre")
        print("2. Ganancias")
        print("3. Fecha de apertura")
        eleccion = input("Elige opción: ")

        if eleccion == "1":
            print("\n===== ORDENADOS POR NOMBRE =====")
            for e in biblioteca.ordenar_nombre():
                print(e)

        elif eleccion == "2":
            print("\n===== ORDENADOS POR GANANCIAS =====")
            for e in biblioteca.ordenar_ganancias():
                print(f"{e.nombre} -> {e.ganancias}")

        elif eleccion == "3":
            print("\n===== ORDENADOS POR FECHA =====")
            for e in biblioteca.ordenar_apertura():
                print(f"{e.nombre} -> {e.fecha_apertura}")

    elif opcion.lower() == "a":
        print("\n===== AÑADIR ESTUDIO =====")
        id = int(input("ID: "))
        nombre = input("Nombre: ")
        ganancias = float(input("Ganancias: "))
        nuevo = Estudio(id, nombre, [], date(2000,1,1), True, None, ganancias, date.today())
        biblioteca.añadir_estudio(nuevo)

    else:
        id = int(opcion)

        if id < 0:
            if biblioteca.eliminar_estudio(abs(id)):
                print("Estudio eliminado.")
            else:
                print("ID no encontrado.")

        else:
            for e in biblioteca.estudios:
                if e.id == id:
                    while True:
                        print("\n--- FICHA DEL ESTUDIO ---")
                        print(f"1. Nombre: {e.nombre}")
                        print(f"2. Fundadores: {e.fundadores}")
                        print(f"3. Fecha de apertura: {e.fecha_apertura}")
                        print(f"4. Estado abierto: {e.abierto}")
                        print(f"5. Fecha de cierre: {e.fecha_cierre}")
                        print(f"6. Ganancias: {e.ganancias}")
                        print(f"7. Último Estreno: {e.ultimo_estreno}")
                        print("0. Volver")

                        opcion = input("Selecciona una opción: ")

                        if opcion == "0":
                            break

                        elif opcion == "1":
                            nuevo = input("Nuevo nombre: ")
                            biblioteca.cambia_nombre(nuevo, id)

                        elif opcion == "2":
                            print(e.fundadores)
                            eleccion = input("Quieres añadir o eliminar? ")
                            if eleccion.lower() == "añadir":
                                nuevo_fundador = input("Escribe el nombre: ")
                                e.fundadores.append(nuevo_fundador)
                            elif eleccion.lower() == "eliminar":
                                borrar_fundador = input("A quien quieres eliminar: ")
                                e.fundadores.remove(borrar_fundador)
                            

                        elif opcion == "3":
                            año = int(input("Escribe el año: "))
                            mes = int(input("Escribe el mes: "))
                            dia = int(input("Escribe el dia: "))
                            nueva_apertura = date(año, mes, dia)
                            e.fecha_apertura = nueva_apertura
                            print(f"La fecha de apertura ha sido cambiada a {e.fecha_apertura}")

                        elif opcion == "4":
                            biblioteca.actualiza_estado(id, not e.abierto)

                        elif opcion == "5":
                            año = int(input("Escribe el año: "))
                            mes = int(input("Escribe el mes: "))
                            dia = int(input("Escribe el dia: "))
                            cierre = date(año, mes, dia)
                            e.fecha_cierre = cierre
                            print(f"La fecha de cierre ha sido cambiada a {e.fecha_cierre}")

                        elif opcion == "6":
                            nueva_ganacia = int(input("Escriba la nueva cantidad en millones: "))
                            e.ganancias = nueva_ganacia

                        elif opcion == "7":
                            año = int(input("Escribe el año: "))
                            mes = int(input("Escribe el mes: "))
                            dia = int(input("Escribe el dia: "))
                            nuevo_estreno = date(año, mes, dia)
                            e.ultimo_estreno = nuevo_estreno
                            print(f"El último estreno ha sido cambiado a {e.ultimo_estreno}")