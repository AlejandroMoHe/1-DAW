from Planeta import Planeta
from datetime import datetime

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

planetas_trappist = [
    Planeta("TRAPPIST-1b", 0.85 * 5.972e24, 1.116 * 6.371e6, datetime(2017, 2, 22), []),

    Planeta("TRAPPIST-1c", 1.38 * 5.972e24, 1.097 * 6.371e6, datetime(2017, 2, 22), []),

    Planeta("TRAPPIST-1d", 0.388 * 5.972e24, 0.788 * 6.371e6, datetime(2017, 2, 22), []),

    Planeta("TRAPPIST-1e", 0.692 * 5.972e24, 0.920 * 6.371e6, datetime(2017, 2, 22), []),

    Planeta("TRAPPIST-1f", 1.04 * 5.972e24, 1.045 * 6.371e6, datetime(2017, 2, 22), []),

    Planeta("TRAPPIST-1g", 1.32 * 5.972e24, 1.127 * 6.371e6, datetime(2017, 2, 22), []),

    Planeta("TRAPPIST-1h", 0.326 * 5.972e24, 0.755 * 6.371e6, datetime(2017, 2, 22), [])
]

#Apartado 1

masa_media_sistema_solar = sum([p.masa for p in planetas]) / len(planetas)
masa_media_trappist = sum([p.masa for p in planetas_trappist]) / len(planetas_trappist)
print(f'La masa media de los planetas del Sistema Solar es: {masa_media_sistema_solar} mientras que la de Trappist1 es: {masa_media_trappist}')

#Apartado 2

todos_planetas = planetas + planetas_trappist
max_densidad = max([p.get_densidad for p in todos_planetas])
planeta_mas_denso = todos_planetas[0]
for p in todos_planetas:
    if p.get_densidad() == planeta_mas_denso.get_densidad():
        planeta_mas_denso = p
        break
print(f'El planeta más denso es: {planeta_mas_denso.nombre} con una densidad de {planeta_mas_denso.get_densidad()}')

#Apartado 3
densidad_tierra = 0
for p in planetas:
    if p.nombre == "Tierra":
        densidad_tierra = p.get_densidad
        break

for p in planetas_trappist:
    