from BibliotecaEstudios import BibliotecaEstudios
import datos

occidente = datos.get_datos(0)
oriente = datos.get_datos(1)

biblioteca = BibliotecaEstudios(1, "Prueba", [occidente])
print(biblioteca)