Algoritmo calculatronAMH
	contCorect<-0
	dificultad<-1
	vidasNormal<-3
	Repetir
		Escribir "Bienvenido/a a Calculatron, elige una opción:"
		Escribir "1. Jugar"
		Escribir "2. Configurar"
		Escribir "0. Salir"
		Leer opcMenu
		Segun opcMenu Hacer
			1:
				Repetir
					vidas<-vidasNormal
					Mientras dificultad=1 y vidas>0 Hacer
						num1<-azar(11)
						num2<-azar(11)
						ope<-azar(3)
						Segun ope Hacer
							0:
								Escribir "Resuelve: ",num1, " + ", num2," ="
								Leer respuesta
								solucion <- num1+num2
							1:
								Escribir "Resuelve: ",num1, " - ", num2," ="
								Leer respuesta
								solucion <- num1-num2
							2:
								Escribir "Resuelve: ",num1, " * ", num2," ="
								Leer respuesta
								solucion <- num1*num2
						Fin Segun
						Si respuesta<>solucion Entonces
							vidas<-vidas-1
							Escribir "Has fallado!"
							Escribir "El resultado era: ",solucion
							Escribir "Te quedan ",vidas," vidas"
						SiNo
							contCorect<-contCorect+1
						Fin Si
						Si vidas=0 Entonces
							Escribir "Has acertado un total de ", contCorect, " cuentas"
						Fin Si
					Fin Mientras
					Mientras dificultad=2 y vidas>0 Hacer
						num1D<-azar(21)
						num2D<-azar(21)
						Segun ope Hacer
							0:
								Escribir "Resuelve: ",num1D, " + ", num2D," ="
								Leer respuesta
								solucion <- num1D+num2D
							1:
								Escribir "Resuelve: ",num1D, " - ", num2D," ="
								Leer respuesta
								solucion <- num1D-num2D
							2:
								Escribir "Resuelve: ",num1D, " * ", num2D," ="
								Leer respuesta
								solucion <- num1D*num2D
						Fin Segun
						Si respuesta<>solucion Entonces
							vidas<-vidas-1
							Escribir "Has fallado!"
							Escribir "El resultado era: ",solucion
							Escribir "Te quedan ",vidas," vidas"
						SiNo
							contCorect<-contCorect+1
						Fin Si
						Si vidas=0 Entonces
							Escribir "Has acertado un total de ", contCorect, " cuentas"
						Fin Si
					Fin Mientras
				Hasta Que vidas=0
				
			2:
				Repetir
					Escribir "La configuración actual es:"
					Escribir "Numero de vidas: ", vidasNormal, " vidas"
					Si dificultad=1 Entonces
						Escribir "Nivel de dificultad: Normal"
					SiNo
						Escribir "Nivel de dificultad: Dificil"
					Fin Si
					Escribir "Deseas cambiar algo? "
					Escribir "1. Cambiar numero de vidas: "
					Escribir "2. Cambiar dificultad: "
					Escribir "0. Salir configuración "
					Leer opcConfig
					Segun opcConfig Hacer
						1:
							Escribir "Inserta un numero valido (entre 1 y 10)"
							Leer vidasNormal
							Mientras vidasNormal<1 o vidasNormal>10 Hacer
									Escribir "Inserta un numero valido (entre 1 y 10)"
									Leer vidasNormal
							Fin Mientras
						2:
							Escribir "Inserta una dificultad valida (1=Normal, 2=Dificil)"
							Leer dificultad
							Mientras dificultad>2 o dificultad<1 Hacer
									Escribir "Inserta una dificultad valida (1=Normal, 2=Dificil)"
									Leer dificultad
							Fin Mientras
					Fin Segun
				Hasta Que opcConfig=0
		Fin Segun
	Hasta Que opcMenu=0
FinAlgoritmo
