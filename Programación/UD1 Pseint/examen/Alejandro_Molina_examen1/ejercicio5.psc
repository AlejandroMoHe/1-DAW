Algoritmo ejercicio5
	Escribir "Introduce la primera palabra: "
	Leer palabra1
	Escribir "Introduce la segunda palabra: "
	Leer palabra2
	Si Longitud(palabra1)>Longitud(palabra2) Entonces
		Escribir "La primera palabra ", "(",palabra1,")", " tienes mas letras (", Longitud(palabra1), ") que la segunda palabra ","(",palabra2,") que tiene (", Longitud(palabra2),") letras."
	SiNo
		Si Longitud(palabra1)<Longitud(palabra2) Entonces
			Escribir "La segunda palabra (",palabra2,") tienes mas letras (", Longitud(palabra2), ") que la primera palabra (",palabra1,") que tiene (", Longitud(palabra1),") letras."
		SiNo
			Escribir "Ambas palabras (",palabra1,") y (", palabra2,") tienen el mismo numero de letras (", Longitud(palabra1),")."
		Fin Si
	Fin Si
FinAlgoritmo
