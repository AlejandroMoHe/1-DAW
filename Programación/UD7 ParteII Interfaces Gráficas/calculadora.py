import tkinter as tk

def click(boton):
    actual = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, actual + str(boton))

def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")

def limpiar():
    pantalla.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Calculadora")

pantalla = tk.Entry(ventana, font=("Arial", 20), bd=10, relief="sunken", justify="right")
pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Cuadrícula completa (todo integrado)
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('C', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('/', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (texto, fila, columna) in botones:
    if texto == "=":
        boton = tk.Button(ventana, text=texto, width=5, height=2, command=calcular)
    elif texto == "C":
        boton = tk.Button(ventana, text=texto, width=5, height=2, command=limpiar)
    else:
        boton = tk.Button(ventana, text=texto, width=5, height=2,
                          command=lambda t=texto: click(t))
    boton.grid(row=fila, column=columna, padx=2, pady=2)

ventana.mainloop()