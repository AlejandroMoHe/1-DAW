import math


def area_cuadrado(lado: float) -> float:
    '''
    :lado: un valor entero o decimal
    :return: multiplica lado por lado asin dando el área del número insertado
    '''
    return lado * lado


def perimetro_rectangulo(base: float, altura: float) -> float:
    '''
    :base: un valor entero o decimal representando los lados de arriba y abajo del rectangulo
    :altura: un valor entero o decimal representando los lados izquierdos y derecho del rectangulo
    :return: devuelve los valores cálculados utilizando la formúla del perimetro
    '''
    return 2 * (base + altura)


def area_circulo(radio: float) -> float:
    '''
    :radio: un valor entero o decimal
    :return: devuelve el resultado del área del circulo, esta llamando a la biblioteca de math para utilizar pi 
    '''
    return math.pi * radio * radio


def area_triangulo(base: float, altura: float) -> float:
    '''
    :base: un valor entero o decimal
    :altura: un valor entero o decimal
    :return: devuelve el resultado del área del triangulo,
    '''
    return (base * altura) / 2


def hipotenusa(cateto1: float, cateto2: float) -> float:
    '''
    :cateto1: un valor entero o decimal
    :cateto2: un valor entero o decimal
    :return: devuelve el resultado de la hipotenusa llamando la biblioteca math para usar la raíz cuadrada
    '''
    return math.sqrt(cateto1 ** 2 + cateto2 ** 2)


def distancia_puntos(x1: float, y1: float, x2: float, y2: float) -> float:
    '''
    :x1: un valor entero o decimal
    :y1: un valor entero o decimal
    :x2: un valor entero o decimal
    :y2: un valor entero o decimal
    :return: devuelve la variable distancia
    '''
    dx = x2 - x1
    dy = y2 - y1
    distancia = math.sqrt(dx ** 2 + dy ** 2)
    return distancia


def area_triangulo_lados(a: float, b: float, c: float) -> float:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def es_triangulo_valido(a: float, b: float, c: float) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True


def volumen_prisma_rectangular(ancho: float, fondo: float, altura: float) -> float:
    base = ancho * fondo
    volumen = base * altura
    return volumen


def area_corona_circular(radio_exterior: float, radio_interior: float) -> float:
    area_exterior = math.pi * radio_exterior ** 2
    area_interior = math.pi * radio_interior ** 2
    area = area_exterior - area_interior
    return area