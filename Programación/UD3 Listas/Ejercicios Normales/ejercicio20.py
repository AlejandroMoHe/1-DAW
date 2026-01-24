tareas = [
    "Comprar fruta",
    "Estudiar programación",
    "Desinstalar el LOL"
]

print("Bienvenido a la app de listas to-do más avanzada del universo")

while True:
    print("1. Ver tareas pendientes")
    print("2. Agregar tarea pendiente")
    print("0. Salir")

    opcion = int(input())

    if opcion == 0:
        break

    elif opcion == 1:
        print("-----------------------")
        print("LISTAS TAREAS PENDIENTES:")
        for i, tarea in enumerate(tareas):

            print(f"{i+1} {tarea}")
        print("-----------------------")

    elif opcion == 2:
        tareaNueva = input("¿Qué tarea quieres insertar? ")
        pos = int(input("¿En que posición? "))
        tareas.insert(pos-1,tareaNueva)
