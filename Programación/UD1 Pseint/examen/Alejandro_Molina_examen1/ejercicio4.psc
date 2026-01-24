Algoritmo ejercicio4
	Escribir "¿Cuantas cartas quieres generar?"
	leer numCartas
	Para i<-1 Hasta numCartas Con Paso 1 Hacer
		resultado<-azar(11)
		Escribir "Carta numero ",i," : " resultado
		Segun resultado Hacer
			1:
				Escribir azar1+(7)," de Copas"
			2:
				Escribir azar1+(7) " de Bastos"
			3:
				Escribir azar1+(7) " de Espadas"
			4:
				Escribir azar1+(7) " de Oros"
		Fin Segun
	Fin Para
FinAlgoritmo
