Algoritmo letras
	Escribir "Inserta un numero:"
	Leer num
	Repetir
		Escribir "Inserta una palabra de ", num, " letras"
		Leer palabra
		Si num<>Longitud(palabra) Entonces
			Escribir "He dicho de ",num," letras!!"
			Leer palabra
		Fin Si
	Hasta Que num=Longitud(palabra)
FinAlgoritmo
