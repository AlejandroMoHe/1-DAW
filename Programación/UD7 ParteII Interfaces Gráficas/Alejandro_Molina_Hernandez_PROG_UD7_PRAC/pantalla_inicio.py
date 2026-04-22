import tkinter as tk

class PantallaInicio(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.configure(bg="lightblue")

        titulo = tk.Label(
            self,
            text="Quiz de Animales",
            font=("Arial", 24, "bold"),
            bg="lightblue"
        )
        titulo.pack(pady=40)

        descripcion = tk.Label(
            self,
            text="Resuelve acertijos sobre animales.",
            font=("Arial", 14),
            bg="lightblue"
        )
        descripcion.pack(pady=10)

        boton_jugar = tk.Button(
            self,
            text="Jugar",
            width=20,
            height=2,
            command=lambda: controller.mostrar_pantalla("PantallaQuiz")
        )
        boton_jugar.pack(pady=20)

        boton_config = tk.Button(
            self,
            text="Configuración",
            width=20,
            height=2,
            command=lambda: controller.mostrar_pantalla("PantallaConfiguracion")
        )
        boton_config.pack(pady=10)