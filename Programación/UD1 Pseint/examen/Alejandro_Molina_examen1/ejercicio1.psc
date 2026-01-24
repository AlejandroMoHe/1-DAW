Algoritmo ejercicio1
	Escribir "¿Cuantas veces quieres lanzar la moneda?"
	Leer nTiradas
	Para i<-1 Hasta nTiradas Con Paso 1 Hacer
		tirada<-1+azar(2)
		Si tirada=1 Entonces
			lado<-"cara"
			contCara<-contCara+1
		SiNo
			lado<-"cruz"
			contCruz<-contCruz+1
		Fin Si
		Escribir "Tirada ", i, ": ", lado
	Fin Para
	
	Escribir "Resumen: "
	Escribir "Caras: ", contCara
	Escribir "Cruces: ", contCruz
FinAlgoritmo
