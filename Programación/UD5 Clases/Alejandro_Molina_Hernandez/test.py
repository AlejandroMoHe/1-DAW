from BibliotecaEstudios import BibliotecaEstudios
from datos import get_datos

biblioteca = BibliotecaEstudios(1, "Biblioteca Estudios", get_datos(0))

print("\n===== LISTADO INICIAL =====")
for e in biblioteca.estudios:
    print(e)

print("\n===== AÑADIR ESTUDIO =====")
biblioteca.añadir_estudio(get_datos(1)[0])
for e in biblioteca.estudios:
    print(e)

print("\n===== ELIMINAR ID 1 =====")
biblioteca.eliminar_estudio(1)
for e in biblioteca.estudios:
    print(e)

print("\n===== MODIFICAR ESTADO (ID 2) =====")
biblioteca.actualiza_estado(2, False)
for e in biblioteca.estudios:
    if e.id == 2:
        print(e)

print("\n===== CAMBIAR NOMBRE (ID 3) =====")
biblioteca.cambia_nombre("Nuevo Estudio", 3)
for e in biblioteca.estudios:
    if e.id == 3:
        print(e)

print("\n===== MAYOR GANANCIA =====")
print(biblioteca.mayor_ganancia())

print("\n===== MENOR GANANCIA =====")
print(biblioteca.menor_ganancia())

print("\n===== ORDENADOS POR NOMBRE =====")
for e in biblioteca.ordenar_nombre():
    print(e)

print("\n===== ORDENADOS POR GANANCIAS =====")
for e in biblioteca.ordenar_ganancias():
    print(e)

print("\n===== ORDENADOS POR FECHA APERTURA =====")
for e in biblioteca.ordenar_apertura():
    print(e)

print("\n===== ESTUDIOS ANTIGUOS (<2000) =====")
for e in biblioteca.estudios_antiguos(2000):
    print(e)

print("\n===== AÑOS ABIERTOS =====")
for e, años in biblioteca.años_abierto():
    print(f"{e.nombre} -> {años} años")