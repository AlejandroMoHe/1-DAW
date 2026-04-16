import tkinter as tk
from pantalla_inicio import PantallaInicio
from pantalla_configuracion import PantallaConfiguracion
from pantalla_juego import PantallaQuiz

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Quiz de Animales")
        self.geometry("700x500")
        self.resizable(True, True)

        contenedor = tk.Frame(self)
        contenedor.pack(fill="both", expand=True)

        self.pantallas = {}

        for Pantalla in (PantallaInicio, PantallaConfiguracion, PantallaQuiz):
            nombre = Pantalla.__name__
            frame = Pantalla(contenedor, self)
            self.pantallas[nombre] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_pantalla("PantallaInicio")

    def mostrar_pantalla(self, nombre):
        pantalla = self.pantallas[nombre]

        if nombre == "PantallaQuiz":
            pantalla.cargar_config()

        pantalla.tkraise()

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()