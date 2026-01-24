via = input("Dime una via (autovia o nacional): ")
vehiculo = input("Cual es tu vehiculo (coche, autobus, camion): ")

if via == "autovia":
    if vehiculo == "coche":
        print("120km/h")
    elif vehiculo == "autobus":
        print("110km/h")
    elif vehiculo == "camion":
        print("100km/h")
elif via == "nacional":
    if vehiculo == "coche":
        print("100km/h")
    elif vehiculo == "autobus":
        print("100km/h")
    elif vehiculo == "camion":
        print("90km/h")