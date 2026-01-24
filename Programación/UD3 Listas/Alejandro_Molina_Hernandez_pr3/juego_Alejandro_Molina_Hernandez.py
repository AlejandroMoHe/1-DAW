import funciones

nivel1 = ["gato", "goma", "leon", "hoja"]
nivel2 = ["puerta", "semana", "italia", "agosto"]
nivel3 = ["pantalla", "elefante", "alemania", "telefono"]

vidas = 10
niveles = [nivel1, nivel2, nivel3]

for n in range(3):
    print("---------------------------")
    print("Nivel", n + 1, "")
    print("---------------------------")

    palabra = funciones.elegirPalabra(niveles[n])
    palabraOculta = funciones.crearOculta(palabra)
    letrasUsadas = []

    while vidas > 0:
        funciones.mostrarEstado(vidas, palabraOculta)
        letra = input("Introduce una letra: ").lower()

        if len(letra) != 1:
            print("Debe ser una letra individual")

        resultado = funciones.comprobarLetra(letra, palabra, palabraOculta, letrasUsadas)
        vidas += resultado

        if resultado > 0:
            print("Has encontrado una letra!! Te sumo una vida")
        else:
            print("Has fallado :(, pierdes una vida)")

        if funciones.palabraResuelta(palabraOculta):
            print("Enhorabuena has encontrado la palabra:")
            print(palabra)
            break

if vidas <= 0:
    print("No quedan vidas")
    print("Has perdido")
else:
    print("Has ganado!!!")
