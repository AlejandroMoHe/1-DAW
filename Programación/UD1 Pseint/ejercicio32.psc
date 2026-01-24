Algoritmo ejercicio32
	Escribir "Inserta un numero:"
	Leer num
	Para i<-num Hasta 1 Con Paso -1 Hacer
		
		Si num MOD i = 0 Entonces
			nDivisores <- nDivisores + 1
		SiNo
		Fin Si
		
		Si nDivisores<=2 Entonces
			Escribir num, " es primo"
		SiNo
			Escribir numu, " NO es primo"
		Fin Si
		
	Fin Para
FinAlgoritmo