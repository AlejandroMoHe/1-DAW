from datetime import datetime
from Planetas import Planeta

#Ejercicio 6
planetas = [
    Planeta("Mercurio", 3.301e23, 2.439e6, datetime.min, []),

    Planeta("Venus", 4.867e24, 6.052e6, datetime.min, []),

    Planeta("Tierra", 5.972e24, 6.371e6, datetime.min, [["Luna", 1.737e6, 7.342e22]]),

    Planeta("Marte", 6.417e23, 3.389e6, datetime.min, [["Fobos", 1.11e4, 1.06e16], ["Deimos", 6.2e3, 1.48e15]]),

    Planeta("Júpiter", 1.898e27, 6.991e7, datetime.min, [["Ío", 1.821e6, 8.93e22], ["Europa", 1.561e6, 4.8e22], ["Ganimedes", 2.634e6, 1.48e23], ["Calisto", 2.410e6, 1.08e23]]),

    Planeta("Saturno", 5.683e26, 5.823e7, datetime.min, [["Titán", 2.575e6, 1.35e23], ["Encélado", 2.52e5, 1.08e20]]),

    Planeta("Urano", 8.681e25, 2.536e7, datetime(1781, 3, 13), [["Titania", 7.89e5, 3.5e21], ["Oberón", 7.61e5, 3.0e21]]),

    Planeta("Neptuno", 1.024e26, 2.462e7, datetime(1846, 9, 23), [["Tritón", 1.353e6, 2.14e22]])
]

#Ejercicio 7

#Apartado 1

densidades = []

for planeta in planetas:
    densidades.append(planeta.get_densidad())

print(densidades)

#Apartado 2

planeta_mas_denso = planetas[0]

for planeta in planetas:
    if planeta.get_densidad() > planeta_mas_denso.get_densidad():
        planeta_mas_denso = planeta

print("Planeta con mayor densidad:", planeta_mas_denso.nombre)


#Apartado 3

radio_luna = 1.737e6
lunas_mas_grandes = []

for planeta in planetas:
    for luna in planeta.lunas:
        if luna[1] > radio_luna:
            lunas_mas_grandes.append(luna[0])

print("Las lunas que son más grandes que La Luna son:", lunas_mas_grandes)

#Apartado 4

radios_lunas = []

for planeta in planetas:
    for luna in planeta.lunas:
        radios_lunas.append(luna[1])

radio_min = min(radios_lunas)

for planeta in planetas:
    for luna in planeta.lunas:
        if luna[1] == radio_min:
            print("Luna más pequeña:", luna[0])
            break


