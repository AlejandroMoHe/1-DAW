#Ejercicio 3
import datos
from datetime import date
from Empleado import Empleado

def media_sueldo(empleados: list[Empleado]) -> float:
    sumatoria = 0
    for e in empleados:
        sumatoria += e.sueldo/len(empleados)
    return sumatoria


def mayor_sueldo(empleados: list[Empleado]) -> Empleado:
    for e in empleados:

        sueldo_mas_alto = e.sueldo

        if e.sueldo > sueldo_mas_alto:
            sueldo_mas_alto = e.sueldo

    return f"{e.nombre} - {e.sueldo} €"


def mayor_que(empleados: list[Empleado], n: float) -> list[Empleado]:
    sueldos_mayores = []
    for e in empleados:

        if e.sueldo > n:
            sueldos_mayores.append(e.nombre)
    
    return sueldos_mayores


def antiguedad(empleados: list[Empleado], n: int) -> list[Empleado]:
    for e in empleados:
        empleado_mayor = []
        if e.fecha_ingreso > n:
            empleado_mayor.append(e.nombre)


def f3e(empleados: list[Empleado]) -> Empleado:
    pass


def f3f(empleados: list[Empleado]) -> list[Empleado]:
    pass


def f3g(empleados: list[Empleado], anio: int) -> list[Empleado]:
    pass


def f3h(empleados: list[Empleado], departamento: str) -> list[Empleado]:
    pass


def f3i(empleados: list[Empleado]) -> dict[str, int]:
    pass


def f3j(empleados: list[Empleado]) -> dict[str, float]:
    pass


if __name__ == "__main__":
    empleados = datos.get_empleados()

    print(media_sueldo(empleados))
    print(mayor_sueldo(empleados))
    print(mayor_que(empleados, 2000))