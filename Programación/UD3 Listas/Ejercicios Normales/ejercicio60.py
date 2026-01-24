pacientes = {
    'Alberto': 'Brazo roto',
    'Maria': 'Gripe',
    'Pedro': 'Covid'
}

horaCita = {
    'Alberto': '11:26',
    'Maria': '10:45',
    'Pedro': '9:35'
}

nombre = input("Inserte el nombre del paciente? ")

while True:
    print("1. Problema")
    print("2. Hora de la cita")
    print("0. Cerrar")

    opcion = int(input("Que quiere saber? "))

    if opcion == 0:
        break

    if opcion == 1:
        if nombre in pacientes:
            print(f"El paciente {nombre} tiene {pacientes[nombre]}")
        else:
            pacienteNuevo = nombre
            problema = input("Cúal es lo que le pasa: ")

            pacientes[pacienteNuevo] = problema

    elif opcion == 2:
        if nombre in horaCita:
            print(f"El paciente {nombre} tiene cita a las {horaCita[nombre]}")
        else:
            print("El paciente no tiene cita guardada")
            hora= input("A que hora tiene la cita")
            horaCita[nombre] = hora

        
