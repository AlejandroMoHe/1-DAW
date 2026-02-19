#Ejercicio 4
import datos


empleados = datos.get_empleados()
mejor_empleado = []
for empleado in empleados:
    actual = empleado
    if len(empleado.empleado_del_mes) > len(actual.empleado_del_mes):
        mejor_empleado.append(actual.nombre)

print(mejor_empleado)