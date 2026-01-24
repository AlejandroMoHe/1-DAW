Algoritmo ejercicio27
	contSecr<-64
	nIntentos<-1
	Escribir "Adivina el numero secreto"
	Repetir
		Leer contInt
		Si contInt<>contSecr Entonces
			nIntentos<-nIntentos + 1
			Si contInt<contSecr Entonces
				Escribir "El numero es mayor, prueba denuevo"
			SiNo
				Escribir "El numero es menor, prueba denuevo"
			Fin Si
		Fin Si
	Hasta Que contSecr=contInt
	Escribir "Felicidades!!! los has adivinado en ",nIntentos," intentos el numero secreto era ",contSecr
FinAlgoritmo

