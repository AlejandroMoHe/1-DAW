# pantalla_quiz.py

import tkinter as tk
import json
import os
import random

class PantallaQuiz(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.preguntas = [
            {
                "acertijo": "Tengo el cuello muy largo y manchas por todo el cuerpo. ¿Qué animal soy?",
                "respuesta": "jirafa"
            },
            {
                "acertijo": "Soy el rey de la selva y tengo melena. ¿Qué animal soy?",
                "respuesta": "leon"
            },
            {
                "acertijo": "Tengo ocho brazos y vivo en el mar. ¿Qué animal soy?",
                "respuesta": "pulpo"
            },
            {
                "acertijo": "Salto mucho, tengo una bolsa y vivo en Australia. ¿Qué animal soy?",
                "respuesta": "canguro"
            },
            {
                "acertijo": "Tengo rayas negras y blancas y me parezco a un caballo. ¿Qué animal soy?",
                "respuesta": "cebra"
            }
        ]

        random.shuffle(self.preguntas)

        self.indice = 0
        self.puntuacion = 0
        self.vidas = 3

        self.configure(bg="#dff6ff")

        self.label_titulo = tk.Label(
            self,
            text="Quiz de Animales",
            font=("Arial", 24, "bold"),
            bg="#dff6ff",
            fg="#003049"
        )
        self.label_titulo.pack(pady=20)

        self.label_vidas = tk.Label(
            self,
            text=f"Vidas: {self.vidas} ❤️",
            font=("Arial", 14, "bold"),
            bg="#dff6ff",
            fg="red"
        )
        self.label_vidas.pack()

        self.label_puntuacion = tk.Label(
            self,
            text=f"Puntuación: {self.puntuacion}",
            font=("Arial", 14),
            bg="#dff6ff",
            fg="#003049"
        )
        self.label_puntuacion.pack(pady=5)

        self.frame_pregunta = tk.Frame(self, bg="white", bd=3, relief="ridge")
        self.frame_pregunta.pack(pady=20, padx=40, fill="x")

        self.label_pregunta = tk.Label(
            self.frame_pregunta,
            text="",
            font=("Arial", 16),
            bg="white",
            wraplength=500,
            pady=20
        )
        self.label_pregunta.pack()

        self.entry_respuesta = tk.Entry(
            self,
            width=30,
            font=("Arial", 14),
            justify="center"
        )
        self.entry_respuesta.pack(pady=15)

        self.label_resultado = tk.Label(
            self,
            text="",
            font=("Arial", 13, "bold"),
            bg="#dff6ff"
        )
        self.label_resultado.pack(pady=10)

        boton_comprobar = tk.Button(
            self,
            text="Comprobar respuesta",
            font=("Arial", 12, "bold"),
            bg="#90e0ef",
            fg="black",
            width=20,
            command=self.comprobar_respuesta
        )
        boton_comprobar.pack(pady=10)

        boton_inicio = tk.Button(
            self,
            text="Volver al inicio",
            font=("Arial", 12),
            bg="#caf0f8",
            width=20,
            command=lambda: controller.mostrar_pantalla("PantallaInicio")
        )
        boton_inicio.pack(pady=10)

        self.cargar_config()
        self.mostrar_pregunta()

    def cargar_config(self):
        color = "#dff6ff"
        nombre = "Jugador"

        if os.path.exists("config.json"):
            with open("config.json", "r") as archivo:
                config = json.load(archivo)
                color = config.get("color", "#dff6ff")
                nombre = config.get("nombre", "Jugador")

        self.configure(bg=color)
        self.label_titulo.config(
            text=f"Quiz de {nombre}",
            bg=color
        )
        self.label_vidas.config(bg=color)
        self.label_puntuacion.config(bg=color)
        self.label_resultado.config(bg=color)

        random.shuffle(self.preguntas)
        self.indice = 0
        self.puntuacion = 0
        self.vidas = 3

        self.label_vidas.config(text=f"Vidas: {self.vidas} ❤️")
        self.label_puntuacion.config(text=f"Puntuación: {self.puntuacion}")
        self.label_resultado.config(text="")

        self.entry_respuesta.pack(pady=15)
        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        if self.vidas <= 0:
            self.label_pregunta.config(
                text=f"Te has quedado sin vidas.\nPuntuación final: {self.puntuacion}"
            )
            self.entry_respuesta.pack_forget()
            return

        if self.indice < len(self.preguntas):
            self.label_pregunta.config(
                text=self.preguntas[self.indice]["acertijo"]
            )
            self.entry_respuesta.delete(0, tk.END)
        else:
            self.label_pregunta.config(
                text=f"¡Has terminado el quiz!\nPuntuación final: {self.puntuacion}/{len(self.preguntas)}"
            )
            self.entry_respuesta.pack_forget()

    def comprobar_respuesta(self):
        if self.indice >= len(self.preguntas) or self.vidas <= 0:
            return

        respuesta_usuario = self.entry_respuesta.get().lower().strip()
        respuesta_correcta = self.preguntas[self.indice]["respuesta"]

        if respuesta_usuario == respuesta_correcta:
            self.puntuacion += 1
            self.label_resultado.config(
                text="¡Correcto!",
                fg="green"
            )
        else:
            self.vidas -= 1
            self.label_resultado.config(
                text=f"Incorrecto. Era: {respuesta_correcta}",
                fg="red"
            )

        self.label_vidas.config(text=f"Vidas: {self.vidas} ❤️")
        self.label_puntuacion.config(text=f"Puntuación: {self.puntuacion}")

        self.indice += 1
        self.after(1500, self.mostrar_pregunta)