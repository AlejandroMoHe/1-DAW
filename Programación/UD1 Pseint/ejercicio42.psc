Algoritmo ejercicio42
	
	Repetir
		num1<-azar(11)
		num2<-azar(11)
		ope<-azar(3)
		
		Segun ope Hacer
			0:
				Escribir "Resuelve: ",num1, " + ", num2," ="
				Leer respuesta
				solucion <- num1+num2
			1:
				Escribir "Resuelve: ",num1, " - ", num2," ="
				Leer respuesta
				solucion <- num1-num2
			2:
				Escribir "Resuelve: ",num1, " * ", num2," ="
				Leer respuesta
				solucion <- num1*num2
		Fin Segun
		Si respuesta=solucion Entonces
			Escribir "Muy bien!!"
		SiNo
			Escribir "Respuesta equivocada, probemos otra vez"
		Fin Si
	Hasta Que respuesta=solucion
	
	
FinAlgoritmo
