# Lista con los nombres de los planetas del sistema solar
planetas_sistema_solar = [
   "Mercurio", "Venus", "Tierra", "Marte",
   "Júpiter", "Saturno", "Urano", "Neptuno"
]


# Lista con las masas de los planetas en kilogramos (valores aproximados)
masas_sistema_solar = [
   3.3011e23,  # Mercurio
   4.8675e24,  # Venus
   5.97237e24, # Tierra
   6.4171e23,  # Marte
   1.8982e27,  # Júpiter
   5.6834e26,  # Saturno
   8.6810e25,  # Urano
   1.02413e26  # Neptuno
]

#Encuentro el planeta más pesado

masPesado = planetas_sistema_solar[0]
mayor = masas_sistema_solar[0]

for i, masa in enumerate(masas_sistema_solar):
   if masa > mayor:
      mayor = masa
      masPesado = i

sumatoria = 0

for masa in masas_sistema_solar:
   sumatoria = sumatoria + masa

media = sumatoria / len(masas_sistema_solar)
