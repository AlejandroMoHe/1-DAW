from datos import get_usuarios
from datos import get_juegos
import funcs
import Usuario



for usuario in get_usuarios():
    user = input("Login: ")
    if usuario.nombre != user:
        print("El nombre de usuario no existe")
        user = input("Inserte de nuevo el nombre: ")

    contraseña = input("Contraseña: ")
    if usuario.contra != contraseña:
        contraseña = input("Contraseña Incorrecta, inserte de nuevo la contraseña: ")
    break

while True:
    funcs.imprimir_juegos()
