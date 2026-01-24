Algoritmo examen1_ejercicio3
	Repetir
		Escribir "¿Que operacion quieres realizar?"
		Escribir "1. Sumar"
		Escribir "2. Restar"
		Escribir "3. Multiplicar"
		Escribir "4. Dividir"
		Escribir "5. Resto"
		Escribir "0. Salir"
		Leer respuesta
		Escribir "Inserta el primer numero"
		Leer num1
		Escribir "Inserta el segundo numero"
		Leer num2
		Segun respuesta Hacer
			1:
				Escribir num1, " + ", num2 " = ", num1+num2
			2:
				Escribir num1, " - ", num2 " = ", num1-num2
			3:
				Escribir num1, " x ", num2 " = ", num1*num2
			4:
				Escribir num1, " dividido ", num2 " = ", num1/num2
			5:
				Escribir "El resto de dividir ", num1," entre ", num2, " es:", num1 MOD num2
		Fin Segun
	Hasta Que respuesta=0
	
FinAlgoritmo