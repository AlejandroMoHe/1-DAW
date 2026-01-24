Algoritmo ejercicio24_doWhile_26
	Escribir "Inserte su nombre:"
	Leer nombre
	
	Repetir
		Escribir "Inserta tu contraseña:"
		Leer pass1
		Escribir "Vuelve a repetir tu contraseña:"
		Leer pass2
		
		Si pass1 <> pass2 Entonces
			acciones_por_verdadero
		SiNo
			acciones_por_falso
		Fin Si
		
	Hasta Que pass1 = pass2
	
FinAlgoritmo
