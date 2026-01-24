from Videojuego import Videojuego


v1 = Videojuego(
   "Resident Evil",
   ["Terror", "Acción"],
   "5/5/1996",
   9.6,
   18,
   10.99,
   1.45
)


v2 = Videojuego(
   "My Little Pony",
   ["Aventura", "Family Friendly"],
   "19/5/2019",
   7.6,
   3,
   20.99,
   8.45
)

#Imprimir objeto entero
print(v)

#Imprimir un solo atributo
#print(v."Atributo")

#Imprimir un metodo
#print(v."Metodo")
'''
Si es una lista se puede modificar

v.puntuacion = 9.7
v.generos.append("Aventura")
print(v)

Como ejecutar los metodos

print(v.precio_final(0.21, 0))
'''