Algoritmo examen1_ejercicio6
	Escribir "Inserta tu nombre de usuario:"
	Leer usuario
	Repetir
		Escribir "Escribe tu contraseña"
		Leer contraseña
		Mientras Longitud(contraseña)<8 Hacer
			Escribir "La contraseña debe tener 8 o mas caracteres"
			Leer contraseña
		Fin Mientras
		Escribir "Repite tu contraseña"
		Leer contraseña2
		Si contraseña<>contraseña2 Entonces
			Escribir "Las contraseñas no coinciden"
		Fin Si
	Hasta Que contraseña=contraseña2
FinAlgoritmo
