from BibliotecaEstudios import BibliotecaEstudios
import datos

occidente = datos.get_datos(0)
oriente = datos.get_datos(1)

biblioteca = BibliotecaEstudios(1, "Prueba", [occidente])

opcion = int(input("Que estudio quieres cambiar?"))
cambio = input("Sigue abierto el estudio?(S/N) ")

BibliotecaEstudios.actualiza_estado(opcion, cambio)

#eleccion = input("Que estudio quieres cambiarle el nombre?")
#nuevo = input(int("Escribe el nuevo nombre: "))