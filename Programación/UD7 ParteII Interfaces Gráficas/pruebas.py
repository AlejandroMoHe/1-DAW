import tkinter as tk
import random

TAM = 50

# Crear ruta (tipo tablero serpiente)
ruta = []
for y in range(1, 9):
    fila = list(range(1, 9))
    if y % 2 == 0:
        fila.reverse()
    for x in fila:
        ruta.append((x, y))

class Juego:
    def __init__(self, root):
        self.root = root
        self.turno = 0
        self.posiciones = [0, 0]
        self.monedas = [0, 0]

        self.canvas = tk.Canvas(root, width=500, height=500, bg="#1abc9c")
        self.canvas.pack()

        self.info = tk.Label(root, text="Turno jugador 1", font=("Arial", 12))
        self.info.pack()

        self.btn = tk.Button(root, text="🎲 Tirar dado", command=self.turno_juego)
        self.btn.pack()

        self.dibujar_tablero()

        self.fichas = [
            self.canvas.create_oval(0,0,0,0, fill="red"),
            self.canvas.create_oval(0,0,0,0, fill="blue")
        ]

        self.actualizar_fichas()

    def dibujar_tablero(self):
        for i, (x,y) in enumerate(ruta):
            tipo = random.choice(["normal", "buena", "mala"])

            if tipo == "normal":
                color = "#ecf0f1"
            elif tipo == "buena":
                color = "#2ecc71"
            else:
                color = "#e74c3c"

            self.canvas.create_rectangle(
                x*TAM, y*TAM, x*TAM+TAM, y*TAM+TAM,
                fill=color, outline="black"
            )

    def actualizar_fichas(self):
        for i, pos in enumerate(self.posiciones):
            x, y = ruta[pos]
            self.canvas.coords(
                self.fichas[i],
                x*TAM+10, y*TAM+10,
                x*TAM+TAM-10, y*TAM+TAM-10
            )

    def evento_casilla(self, jugador):
        evento = random.choice(["+3", "-3", "+5", "-5", "nada"])

        if evento == "+3":
            self.monedas[jugador] += 3
        elif evento == "-3":
            self.monedas[jugador] -= 3
        elif evento == "+5":
            self.monedas[jugador] += 5
        elif evento == "-5":
            self.monedas[jugador] -= 5

        return evento

    def turno_juego(self):
        dado = random.randint(1,6)
        j = self.turno

        self.posiciones[j] += dado

        if self.posiciones[j] >= len(ruta):
            ganador = 0 if self.monedas[0] > self.monedas[1] else 1
            self.info.config(
                text=f"🏆 Fin del juego. Gana jugador {ganador+1} con {self.monedas[ganador]} monedas"
            )
            return

        evento = self.evento_casilla(j)

        self.actualizar_fichas()

        self.turno = (self.turno + 1) % 2

        self.info.config(
            text=f"Jugador {j+1} sacó {dado}, evento {evento} | 💰 J1:{self.monedas[0]} J2:{self.monedas[1]}"
        )

root = tk.Tk()
root.title("Mini Mario Party")

Juego(root)
root.mainloop()