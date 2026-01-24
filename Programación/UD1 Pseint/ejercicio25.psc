Algoritmo ejercicio25
	contSecr<-64
	nIntentos<-1
	Escribir "Adivina el numero secreto"
	Leer contInt
	Mientras contInt<>contSecr Hacer
		Si contInt<contSecr Entonces
			Escribir "El numero es mayor, prueba denuevo"
		SiNo
			Escribir "El numero es menor, prueba denuevo"
		Fin Si
		nIntentos<-nIntentos + 1
		Leer contInt
	Fin Mientras
	Escribir "Felicidades!!! los has adivinado en ",nIntentos," intentos el numero secreto era ",contSecr
FinAlgoritmo
