try:
    num1 = int(input("Inserta un número: "))
    num2 = int(input("Inserta otro número: "))
except Exception as error:
    print(f"Se ha producido un error del tipo: {error}")
else:
    print(f"La suma de {num1} + {num2} es igual a: {num1+num2}")