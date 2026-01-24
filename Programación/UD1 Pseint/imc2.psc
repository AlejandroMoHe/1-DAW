Algoritmo imc2
	Escribir "Cuanto mides?"
	Leer altura
	Escribir "Cuanto pesas"
	Leer peso
	
	imc<-peso/altura*2
	
	Si imc<18.5 Entonces
		Escribir "Estas bajo de peso"
	SiNo
		Si imc>=18.5 y imc<=24.9 Entonces
			Escribir "Tienes tu peso ideal"
		SiNo
			Si imc>=25 y imc<=29.9 Entonces
				Escribir "Te has pasado un poquito"
			SiNo
				Si imc>=30 Entonces
					Escribir "Tienes obesidad"
				Fin Si
			Fin Si
		Fin Si
	Fin Si
	
FinAlgoritmo
