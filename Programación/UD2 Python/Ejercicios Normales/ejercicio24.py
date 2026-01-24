usuario = input("Escribe el usuario: ")
contr1 = input("Escribe la contraseña: ")
contr2 = input("Vuelve a introducir la contraseña: ")

while contr1 != contr2:
    print("Las contraseñas no conciden, vuelve a introducirla: ")
    contr2 = input()
print("Usuario Creado")