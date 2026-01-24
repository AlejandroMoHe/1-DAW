Algoritmo redondeo
	Escribir "Inserta una cantidad de dinero:"
	Leer din
	euros<-trunc(din)
	centimos<- (euros-din)*100
	Escribir din, " son ",euros, " con ", centimos," centimos"
FinAlgoritmo
