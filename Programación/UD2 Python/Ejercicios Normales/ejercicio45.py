while True:
    precio = float(input("Inserta un precio base: "))
    if precio < 0:
        break
    iva = float(input("Inserta el iva: "))
    coste = precioBase * iva / 100
    precioFinal = round(precioBase + coste,2)
    print(f"El precio final es: {precioFinal}")