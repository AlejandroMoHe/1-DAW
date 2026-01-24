calificación = int(input("Cual es tu calificación? "))
if calificación>=90 :
    print("A")
elif calificación<90 and calificación>80 :
    print("B")
elif calificación<80 and calificación>70 :
    print("C")
elif calificación<70 and calificación>60 :
    print("D")
else:
    print("F")