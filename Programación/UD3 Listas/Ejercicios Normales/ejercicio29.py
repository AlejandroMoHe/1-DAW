liga = ["Real Madrid", "Atlético de Madrid", "FC Barcelona", "Athletic Club",  "Villarreal CF", "RCD Mallorca", "Rayo Vallecano", "Girona FC", "Real Sociedad", "Real Betis", "CA Osasuna", "Sevilla FC", "RC Celta", "Getafe CF", "UD Las Palmas", "CD Leganés", "Deportivo Alavés", "RCD Espanyol", "Valencia CF", "Real Valladolid"]

while True:
    equipo = input("Dime un equipo: ")
    if liga.count(equipo) == 0:
        print("El equipo no existe")
    else:
        print(f"{equipo} esta en la posición: {liga.index(equipo)+1}")