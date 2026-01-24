Algoritmo dosVariables
	Escribir "De que curso eres?"
	Leer cicloNombre
	Escribir "En que curso estás?"
	Leer cicloCurso
	
	Si (cicloNombre="DAW" y cicloCurso=1) o (cicloNombre="DAM" y cicloCurso=1) Entonces
		Escribir "Tienes que dar programación"
	SiNo
		Escribir "No tienes programación"
	Fin Si
	
FinAlgoritmo
