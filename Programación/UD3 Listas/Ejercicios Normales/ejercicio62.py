'''
1. Eliminar mobs repetidos de cada lista.
2. Mobs que aparecen en el Overworld (todos los que no aparecen en el Neher) y son hostiles.
3. Mobs que son pacíficos y aparecen en el Nether
4. Mobs presentes en las tres listas a la vez
5.Todos los mobs que existen en las tres categorías
6. Mobs del Nether que no son hostiles
7. ¿Alguna lista tiene mobs repetidos?
8. Mobs que son hostiles o pacíficos, pero no del Nether

'''

mobs_hostiles = ["Zombie", "Skeleton", "Creeper", "Creeper", "Enderman", "Ghast", "Piglin"]
mobs_pacíficos = ["Cow", "Sheep", "Pig", "Villager", "Villager", "Enderman"]
mobs_del_Nether = ["Ghast", "Piglin", "Hoglin", "Blaze", "Piglin", "Enderman"]

hostiles = set(mobs_hostiles)
pacificos = set(mobs_pacíficos)
nether = set(mobs_del_Nether)

#Apartado 1
print("1. Mobs Pacificos: ", list(pacificos))
print("1. Mobs Hostiles: ", list(hostiles))
print("1. Mobs del Nether: ", list(nether))

#Apartado 2
print("2. Mobs del Overworld: ", list(hostiles - nether))

#Apartado 3
print("3. Pacificos del Nether: ", list(pacificos & nether))

#Apartado 4
print("4. Mobs que estan en las tres listas a la vez: ", list(pacificos & hostiles & nether))

#Apartado 5
print("5. Mobs de las tres listas a la vez: ", list(pacificos | hostiles | nether))

#Apartado 6
print("6. Mobs del Nether que no son hostiles: ", list(nether - hostiles))

#Apartado 7
print("7. Alguna lista con mobs repetidos? ",len(mobs_pacíficos) != len(pacificos) or len(mobs_hostiles) != len(hostiles) or len(mobs_del_Nether) != len(nether))

#Apartado 8
print("8. Mobs hostiles o pacificos sin ser del Nether: ", list(pacificos | hostiles - nether))


