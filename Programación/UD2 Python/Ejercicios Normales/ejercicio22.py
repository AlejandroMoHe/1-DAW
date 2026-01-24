dia = input("Inserta el dia de la semana (L, M, X, J, V, S, D): ")
horaSal = int(input("Inserta la hora de salida/llegada: "))
km = float (input("Cuantos kilometros han sido: "))

if dia == "S":
    if horaSal>=8 and horaSal<=18:
        tarifa = 1.2
    else:
        tarifa= 1.5
    