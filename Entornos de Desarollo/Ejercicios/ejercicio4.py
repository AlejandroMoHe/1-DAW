import math


def areaCirculo(radio: float) -> float:
    if radio <= 0:
        return 0
    else:
        return math.pi * radio * radio
   
def esPrimo(num: int) -> bool:
    
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False


def imc(peso: float, altura: float) -> str:
    resultado = peso / (altura * altura)
    if resultado < 18.5:
        return "Bajo peso"
    if resultado >= 18.5 and resultado < 24.9:
        return "Normal"
    if resultado >= 25 and resultado < 29.9:
        return "Sobrepeso"
    if resultado >= 29.9:
        return "Obesidad"