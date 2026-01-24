import math

def pitagoras(c1: float, c2: float) -> float:
    hipotenusa = math.sqrt(c1*c1+c2*c2)
    return hipotenusa

cateto1 = float(input("Inserta la longitud del primer cateto: "))
cateto2 = float(input("Inserta el otro cateto: "))
hipotenusa = pitagoras(c1, c2)
print(f"La hipotenusa es: {hipotenusa}")