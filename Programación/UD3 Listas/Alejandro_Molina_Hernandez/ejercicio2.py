mermeladas = [
    ["DulceSol Fresa", ["fresa", "limon"], 55, False],
    ["VerdeBosque Arandanos", ["arandanos", "manzana"], 60, True],
    ["CampoClaro Melocoton", ["melocoton", "limon"], 48, True],
    ["SolAndaluz Naranja", ["naranja"], 52, False],
    ["MonteMiel Mango", ["mango", "limon"], 58, False],
    ["EcoHuerta Higo", ["higo"], 45, True],
    ["RocaDulce Ciruela", ["ciruela"], 49, True],
    ["BosqueRojo Frambuesa", ["frambuesa", "manzana"], 62, False],
]

apartadoA = []

media = 0
for mermelada in mermeladas:
    media += mermelada[2]
media /= len(mermeladas)

#Apartados
#A
print("Apartado a):")

for mermelada in mermeladas:
    if mermelada[3] == True:
        apartadoA.append(mermelada[0])
    
print(apartadoA)


#B
print("Apartado b):")
apartadoB = [mermelada[0] for mermelada in mermeladas if mermelada[3] == False and mermelada[1]]
print(apartadoB)


#C
print("Apartado c):")

apartadoC = [mermelada[0] for mermelada in mermeladas if mermelada[2] > media]
print(apartadoC)


#D
print("Apartado d):")

apartadoD = [mermelada[0] for mermelada in mermeladas if mermelada[2] > media and mermelada[3] == False and mermelada[1]]
print(apartadoD)