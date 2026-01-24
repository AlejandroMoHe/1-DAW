Algoritmo alazar_ejercicio_41
	Escribir "Inserta el numero mínimo:"
	Leer min
	Escribir "Inserta el numero máximo"
	Leer max
	Escribir "Cuantos numeros aleatorios entre ",min," y ",max," quieres crear:"
	Leer cantidad
	Para i<-1 Hasta cantidad Con Paso 1 Hacer
		Escribir min+azar(max-min+1)
	Fin Para
FinAlgoritmo
