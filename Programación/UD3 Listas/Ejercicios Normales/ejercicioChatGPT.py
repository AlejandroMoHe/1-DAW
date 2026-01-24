sabores = ["Fresa", "Melocoton", "Arandanos", "Naranja", "Frambuesa", "Mango", "Ciruela", "Albaricoque", "Higo", "Kiwi"]
precios = [2.40, 2.85, 3.10, 2.20, 3.50, 2.95, 2.60, 2.75, 3.00, 2.30]
es_sin_azucar = [False, False, True, False, True, False, False, False, True, False]

sabores_sin_azucar = [sabor for i, sabor in enumerate(sabores) if es_sin_azucar[i]]

precio_minimo = min(precios)
for i, precio in enumerate(precios):
    if precios[i] == 

print(sabores_sin_azucar)
print(f"La mermelada más barata es {precio_minimo} y la más cara es {precio_maximo}")
