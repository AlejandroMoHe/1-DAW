clasicas = ["Fresa", "Melocoton", "Naranja", "Albaricoque", "Ciruela"]
ecologicas = ["Fresa", "Higo", "Ciruela", "Arandanos"]
gourmet = ["Frambuesa", "Arandanos", "Naranja", "Mango"]

clasicas_b = set(clasicas)
ecologicas_b = set(ecologicas)
gourmet_b = set(gourmet)

#A
print(ecologicas_b & gourmet_b)

#B
print((clasicas_b | gourmet_b)- ecologicas_b)

