factorial = int(input("Inserta un numero: "))
num = 2
resultado = 1

while num <= factorial:
    resultado = resultado * num
    num = num + 1

print(f"El factorial de {factorial} es: {resultado}")