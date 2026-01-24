Algoritmo ejercicio2
	Repetir
		Escribir "-----------------"
		Escribir "0) Salir"
		Escribir "1) Convertir euros a dólares"
		Escribir "2) Convertir dólares a euros"
		Escribir "3) Convertir euros a libras"
		Escribir "------------------"
		Escribir "Elige una opcion:: "
		Leer eleccion
		Si eleccion>=1 y eleccion<=3 Entonces
			Segun eleccion Hacer
				1:
					Escribir "Introduzca una cantidad en euros: "
					Leer cantidad
					Escribir cantidad, " euros son ", abs(cantidad/1.1), " dolares."				
				2:
					Escribir "Introduzca una cantidad en dolares: "
					Leer cantidad
					Escribir cantidad, " dolares son ", abs(cantidad/0.9) " euros."
				3:
					Escribir "Introduzca una cantidad en euros: "
					Leer cantidad
					Escribir cantidad, " euros son ", abs(cantidad/0.8), " libras."
					
			Fin Segun
		SiNo
			Si eleccion<>0 Entonces
				Escribir "Opcion no válida."
			Fin Si
		Fin Si
	Hasta Que eleccion=0
	Escribir "Programa terminado."
	
FinAlgoritmo
