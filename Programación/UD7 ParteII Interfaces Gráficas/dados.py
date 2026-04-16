import tkinter as tk
import random
import json
import os

CONFIG_FILE = "config.json"

# Configuración por defecto
default_config = {
    "dice_type": 6,
    "language": "es"
}

# Textos en distintos idiomas
texts = {
    "es": {
        "start": "Comenzar",
        "settings": "Configuración",
        "dice": "Tipo de dado:",
        "roll": "Tirar dado",
        "back": "Volver",
        "language": "Idioma",
        "save": "Guardar"
    },
    "en": {
        "start": "Start",
        "settings": "Settings",
        "dice": "Dice type:",
        "roll": "Roll dice",
        "back": "Back",
        "language": "Language",
        "save": "Save"
    }
}

# Cargar configuración
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return default_config.copy()

# Guardar configuración
def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

class DiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("App de dados")
        self.config = load_config()

        self.main_frame = tk.Frame(root)
        self.main_frame.pack()

        self.show_main_menu()

    def clear(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def t(self, key):
        return texts[self.config["language"]][key]

    def show_main_menu(self):
        self.clear()

        tk.Button(self.main_frame, text=self.t("start"),
                  command=self.show_game).pack(pady=10)

        tk.Button(self.main_frame, text=self.t("settings"),
                  command=self.show_settings).pack(pady=10)

    def show_game(self):
        self.clear()

        tk.Label(self.main_frame,
                 text=f"{self.t('dice')} d{self.config['dice_type']}").pack()

        result_label = tk.Label(self.main_frame, text="")
        result_label.pack(pady=10)

        def roll():
            num = random.randint(1, self.config["dice_type"])
            result_label.config(text=str(num))

        tk.Button(self.main_frame, text=self.t("roll"),
                  command=roll).pack(pady=5)

        tk.Button(self.main_frame, text=self.t("back"),
                  command=self.show_main_menu).pack(pady=5)

    def show_settings(self):
        self.clear()

        tk.Label(self.main_frame, text=self.t("dice")).pack()

        dice_var = tk.IntVar(value=self.config["dice_type"])
        tk.Entry(self.main_frame, textvariable=dice_var).pack()

        tk.Label(self.main_frame, text=self.t("language")).pack()

        lang_var = tk.StringVar(value=self.config["language"])
        tk.OptionMenu(self.main_frame, lang_var, "es", "en").pack()

        def save():
            self.config["dice_type"] = dice_var.get()
            self.config["language"] = lang_var.get()
            save_config(self.config)
            self.show_main_menu()

        tk.Button(self.main_frame, text=self.t("save"),
                  command=save).pack(pady=5)

        tk.Button(self.main_frame, text=self.t("back"),
                  command=self.show_main_menu).pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")  # Tamaño más grande
    root.resizable(False, False)  # Opcional: evitar que se pueda redimensionar
    app = DiceApp(root)
    root.mainloop()