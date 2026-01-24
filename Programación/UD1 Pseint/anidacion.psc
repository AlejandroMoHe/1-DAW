Algoritmo anidacion
	Escribir "Cual es peso de su coche?"
	Leer peso
	Si peso<1000 Entonces
		Escribir "Su coche es ligero"
	SiNo
		Si peso>=1000 y peso<=2000 Entonces
			Escribir "Su coche es de peso medio"
		SiNo
			Si peso>2000 Entonces
				Escribir "Su coche es pesado"
			Fin Si
		Fin Si
	Fin Si
FinAlgoritmo
