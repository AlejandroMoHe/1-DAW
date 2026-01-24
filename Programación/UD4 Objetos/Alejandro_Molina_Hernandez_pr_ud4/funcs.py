#print("[V]er mis juegos""[I]gresar dinero""Ir al [c]arrito""[S]alir")
from datos import get_juegos
import Usuario
import Videojuego
def imprimir_juegos():
    print("JUEGOS DISPONIBLES PARA COMPRAR")
    juegos = [get_juegos()]
    for i, juego in juegos:
        print(f"[i]. {juego.nombre}, precio: {juego.precio_base}")

