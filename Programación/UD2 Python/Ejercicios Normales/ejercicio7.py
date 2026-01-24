ciclo = input("En que ciclo estas? ")
curso = int(input("Y en que curso estas? "))

if ciclo=="DAW" or ciclo=="DAM" and curso=="1" or curso=="2":
    print("Tienes que dar programación")
else :
    print("No tienes que dar programación")