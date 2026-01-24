edad = int(input("Cuanto años tienes? "))
if edad<=2:
    print("Bebé")
elif edad>2 and edad<=12:
    print("Niño")
elif edad>12 and edad<=17:
    print("Adolescente")
elif edad>17 and edad<=34:
    print("Adulto pero no")
elif edad==35 :
    print("La mejor edad posible")
elif edad>35 and edad<=50:
    print("Adulto")
elif edad>50 and edad<=67:
    print("Pre-Anciano")
elif edad>67 and edad<=99:
    print("Anciano")
else:
    print("Centenario")