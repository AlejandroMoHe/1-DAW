hora = int(input("Inserta un hora en formanto AM/PM: "))
minutos = int(input("Inserta los minutos: "))
periodo = input("Inserta el periodo (AM/PM) ")


if periodo == "AM":
    hora24 = hora
elif periodo == "PM":
    hora24 = hora +12
else:
    print("Periodo no valido")

if hora24 < 10:
    hora_txt = "0"+str(hora24)

if minutos < 10:
    minutos_txt = "0"+str(minutos)

print(f"{hora}:{minutos} {periodo} son las {hora_txt}:{minutos_txt}")