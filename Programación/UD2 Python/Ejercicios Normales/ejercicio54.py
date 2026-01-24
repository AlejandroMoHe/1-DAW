def factorial(n: int)-> int:
    resultado = 1
    for i in range(2, num+1):
        resultado = resultado * i
        return resultado
num = int(input("Inserta un numero: "))
resultado = factorial(num)
print(f"El factorial de {num} es {resultado}")