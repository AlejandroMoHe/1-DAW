from CursoPresencial import CursoPresencial
from CursoOnline import CursoOnline


cp1 = CursoPresencial(1, "POO Avanzada", 6, "Dr. Pérez", None, 3, "C/Mayor 12", "Aula 2.4", None,)
cp2 = CursoPresencial(2, "Bases de Datos", 5, "Dra. López", None, 2, "C/Norte 8", "Aula 1.1", None)
co1 = CursoOnline(3, "Python Web", 4, "Ing. Ramos", None, 5, "Moodle", "https://moodle.com/python")
co2 = CursoOnline(4, "Docker Básico", 3, "Ing. Díaz", None, 4, "Classroom", "https://classroom.com/docker")

print("=== ESTADO INICIAL DE LOS CURSOS ===")
print(cp1)
print(cp2)
print(co1)
print(co2)
print()
'''
print("=== MATRICULAMOS ALUMNOS EN CURSO PRESENCIAL (ID 1) ===")
print("Intentamos matricular alumnos con ID: 101, 102, 103 y 104")
print(f"Resultado matrícula 101: {cp1.matricular(101)}")
print(f"Resultado matrícula 102: {cp1.matricular(102)}")
print(f"Resultado matrícula 103: {cp1.matricular(103)}")
print(f"Resultado matrícula 104 (debería fallar por falta de plazas): {cp1.matricular(104)}")
print()

print("=== MATRICULAMOS ALUMNOS EN CURSO ONLINE (ID 3) ===")
print("Intentamos matricular alumnos con ID: 201 y 202")
co1.matricular(201)
co1.matricular(202)
print(co1)
print()
'''
print("=== CÁLCULO DE COSTES ===")
print(f"Coste curso presencial: {cp1.calcular_coste()} €")
print(f"Coste curso online: {co1.calcular_coste()} €\n")


print("=== GENERAMOS REUNIÓN EN CURSO ONLINE ===")
print("Generamos enlace a la reunión (debería ser URL base + 10 dígitos aleatorios)")
print(f"Enlace generado: {co1.generar_reunion()}\n")

print("=== COMPROBAMOS IGUALDAD Y EL HASH ===")
print("Generamos un nuevo curso con el mismo ID que cp1 (ID = 1), \n pero con nombre, profesor, y datos distintos\n")

cp1_duplicado = CursoPresencial(1, "Sistema Informáticos", 6, "Dr. Fernández", None, 3, "C/Mayor 18", "Aula 3.6", None,)

print("Comprobamos igualdad entre cp1 y cp1_duplicado")
print(f"Resultado (debería ser True porque comparten ID): {cp1.__eq__(cp1_duplicado)}\n")

print("Ahora comparamos cp1 con cp2 (ID distintos):")
print(f"Resultado (debería ser False): {cp1.__eq__(cp2)}\n")

print("Creamos un set e introducimos ambos cursos con ID = 1")
print("El set elimina duplicados según __hash__ y __eq__.")
cursos_set = {cp1, cp1_duplicado}
print(f"Longitud del set (debería ser 1): {len(cursos_set)}")
