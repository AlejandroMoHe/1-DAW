import tkinter as tk
import json
import os

class PantallaConfiguracion(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.archivo_config = "config.json"

        self.configure(bg="lightgreen")

        titulo = tk.Label(
            self,
            text="Configuración",
            font=("Arial", 22, "bold"),
            bg="lightgreen"
        )
        titulo.pack(pady=20)

        etiqueta_nombre = tk.Label(
            self,
            text="Nombre del jugador:",
            bg="lightgreen"
        )
        etiqueta_nombre.pack(pady=10)

        self.entry_nombre = tk.Entry(self, width=30)
        self.entry_nombre.pack(pady=5)

        etiqueta_color = tk.Label(
            self,
            text="Color de fondo:",
            bg="lightgreen"
        )
        etiqueta_color.pack(pady=10)

        self.color_var = tk.StringVar()
        self.color_var.set("lightblue")

        menu_colores = tk.OptionMenu(
            self,
            self.color_var,
            "lightblue",
            "lightgreen",
            "lightyellow",
            "lightpink"
        )
        menu_colores.pack(pady=5)

        etiqueta_idioma = tk.Label(
            self,
            text="Idioma:",
            bg="lightgreen"
        )
        etiqueta_idioma.pack(pady=10)

        self.idioma_var = tk.StringVar()
        self.idioma_var.set("es")

        menu_idioma = tk.OptionMenu(
            self,
            self.idioma_var,
            "es",
            "en"
        )
        menu_idioma.pack(pady=5)

        boton_guardar = tk.Button(
            self,
            text="Guardar configuración",
            command=self.guardar_config
        )
        boton_guardar.pack(pady=20)

        boton_volver = tk.Button(
            self,
            text="Volver al inicio",
            command=lambda: controller.mostrar_pantalla("PantallaInicio")
        )
        boton_volver.pack(pady=10)

        self.cargar_config()

    def guardar_config(self):
        config = {
            "nombre": self.entry_nombre.get(),
            "color": self.color_var.get(),
            "idioma": self.idioma_var.get()
        }

        with open(self.archivo_config, "w") as archivo:
            json.dump(config, archivo, indent=4)

    def cargar_config(self):
        if os.path.exists(self.archivo_config):
            with open(self.archivo_config, "r") as archivo:
                config = json.load(archivo)

                self.entry_nombre.delete(0, tk.END)
                self.entry_nombre.insert(0, config.get("nombre", "Jugador"))
                self.color_var.set(config.get("color", "lightblue"))
                self.idioma_var.set(config.get("idioma", "es"))