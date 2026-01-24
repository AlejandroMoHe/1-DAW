pesoCoche = int(input("Cuanto pesa tu coche? "))
if pesoCoche<1000:
    print("Su coche es ligero")
elif pesoCoche>=1000 and pesoCoche<=2000:
    print("Su coche tiene un peso medio")
else :
    print("Su coche es pesado")