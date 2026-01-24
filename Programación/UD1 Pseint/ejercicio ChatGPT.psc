Algoritmo ejercicio_chatGPT
	recuPaso<-1
	Escribir "Quieres dar un paso? (si/no)"
	Leer pasosDa
	
	Mientras pasosDa="si" Hacer
		Si pasosDa="si" Entonces
			Escribir "Quieres dar otro paso (si/no)"
			Leer pasosDa
		SiNo
			Escribir "No damos otro paso"
		Fin Si
		recuPaso<- recuPaso + 1
	Fin Mientras
	Escribir "Hemos dado ", recuPaso, " pasos"
	
FinAlgoritmo
