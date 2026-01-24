usuario = input("Introduce tu nombre: ")
contraCorrecta = False

while not contraCorrecta:
    contra1 = input("Introudce la contraseña: ")
    contra2 = input("Vuelve a escribir la contraseña: ")
    if contra1 == contra2:
        contraCorrecta = True
    else:
        print("Las contraseña no coinciden , vuelve a introducirla")
print("Usuario creado")