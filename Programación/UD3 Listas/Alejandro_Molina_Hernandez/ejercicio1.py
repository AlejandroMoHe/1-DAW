sabores = ["Fresa", "Melocoton", "Naranja", "Arandanos", "Higo", "Albaricoque", "Mango", "Frambuesa", "Ciruela", "Limon"]
azucar = [55, 48, 52, 60, 45, 50, 58, 62, 49, 47]
es_light = [False, True, False, False, True, True, False, False, True, True]

apartadoA = [mermelada for i, mermelada in enumerate(sabores) if len(mermelada) <= 6 and es_light[i] == False]
print(apartadoA)

media_azucar = sum(azucar) / len(azucar)
apartadoB = [sabor for i, sabor in enumerate(sabores) if es_light[i] == False and azucar[i] < media_azucar]
print(apartadoB)