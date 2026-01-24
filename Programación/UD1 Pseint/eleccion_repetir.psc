Algoritmo menu
	Repetir
		Escribir "¿Que quieres calcular?"
		Escribir "1. Seno"
		Escribir "2. Coseno"
		Escribir "3. Tangente"
		Escribir "4. Arcoseno"
		Escribir "5. Arcocoseno"
		Escribir "6. Arcotangente"
		Escribir "0. Salir"
		Leer eleccion
		Si eleccion<>0 Entonces
			Escribir "Inserta un angulo:"
			Leer ang_u
		Fin Si

		Segun eleccion Hacer
			1:
				Escribir "El seno de ",ang_u," es ",sen(ang_u)
			2:
				Escribir "El coseno de ",ang_u," es ",cos(ang_u)
			3:
				Escribir "El tangente de ",ang_u," es ",tan(ang_u)
			4:
				Escribir "El arcoseno de ",ang_u," es ",asen(ang_u)
			5:
				Escribir "El arcocoseno de ",ang_u," es ",acos(ang_u)
			6:
				Escribir "El arcotangente de ",ang_u," es ",atan(ang_u)
		Fin Segun
	Hasta Que eleccion=0

FinAlgoritmo
