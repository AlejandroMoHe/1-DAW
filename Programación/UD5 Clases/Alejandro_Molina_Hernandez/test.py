from BibliotecaEstudios import BibliotecaEstudios
import datos

occidente = datos.get_datos(0)
oriente = datos.get_datos(1)

biblioteca = BibliotecaEstudios(1, "Prueba", [occidente])

print(oriente)

#eleccion = input("Que estudio quieres cambiarle el nombre?")
#nuevo = input(int("Escribe el nuevo nombre: "))