while True:
    try:
        
        try:
            num1 = int(input("Inserta un número: "))
        except Exception as error:
            print(f"Se ha producido en la variable num2 un error del tipo: {error}")
        else:
            break

while True:
    try:
        num2 = int(input("Inserta otro número: "))
    except Exception as error:
        print(f"Se ha producido en la variable num1 un error del tipo: {error}")
    else:
        break