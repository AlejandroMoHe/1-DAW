canciones_ana = ["Master of Puppets", "Painkiller", "Hallowed Be Thy Name", "Hallowed Be Thy Name", "Holy Wars", "Chop Suey!"]
canciones_luis = ["Painkiller", "Holy Wars", "Chop Suey!", "Walk", "Walk", "The Trooper"]

set_canciones_ana = set(canciones_ana)
set_canciones_luis = set(canciones_luis)

#Ambas listas sin repetidos
print("Eliminar elementos repetidos en ambas listas.", list(set_canciones_ana), list(set_canciones_luis))

#Canciones de ambos
print("Mostrar las canciones que tienen ambos usuarios.", list(set_canciones_luis & set_canciones_ana))

#Ana pero no Luis
print("Mostrar las canciones que tiene Ana pero no Luis.", list(set_canciones_ana - set_canciones_luis))

#Si tienen repetidos
print("Indicar si alguno de los dos usuarios tiene canciones repetidas en sus listas originales.", len(canciones_luis) != len(set_canciones_luis) or len(canciones_ana) != len(set_canciones_ana))

#Playlist entera
print("Obtener la playlist conjunta, es decir, todas las canciones que tiene Ana o Luis.", list(set_canciones_luis | set_canciones_ana))

#Luis pero no Ana
print("Mostrar las canciones que tiene Luis pero no Ana.", list(set_canciones_luis - set_canciones_ana))
