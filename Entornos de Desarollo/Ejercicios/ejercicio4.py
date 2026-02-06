import math
'''Las importaciones de las bibliotecas van al principio del proyecto
'''

def areaCirculo(area: float) -> float:
    '''Calcula el área de un circulo
    La variable a no era muy intuitiva
    :area: numero real mayor a 0
    :area: float
    :return: devuelme el área calcula con math.pi
    '''
    if area <= 0:
        return 0
    else:
        return math.pi * area * area
   
def esPrimo(num: int) -> bool:
    '''Indica si un número es primo o no
    :num: número entero
    :num: int
    :return: un boleano
    
    '''
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