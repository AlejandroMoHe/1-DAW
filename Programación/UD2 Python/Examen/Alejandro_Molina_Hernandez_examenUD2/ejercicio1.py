cadenaMayor = ""
cadenaMenor = ""
numCadena = 0
recuentoLetras = 0
while True:
    cadena = input("Inserta una cadena de texto: ")

    if cadena == "fin":
        break

    cadenaMenor = cadena

    recuentoLetras = recuentoLetras + len(cadena)

    numCadena = numCadena + 1

    for caracter in cadena:
        if len(cadena) > len(cadenaMayor):
            cadenaMayor = cadena
        elif len(cadena) < len(cadenaMenor):
            cadenaMenor = cadena

if numCadena <1 :
    print("No has insertado ninguna cadena distinta de fin")
else:
    print(f"a) Número de cadenas de texto insertada : {numCadena}")
    print(f"b) Longitud media {recuentoLetras / numCadena} caracteres:")
    print(f"c) La cadena de texto más larga es : {cadenaMayor}")
    print(f"d) La cadena de texto más corta es : {cadenaMenor}")