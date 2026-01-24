real_madrid_jugadores = [
    "Thibaut Courtois",
    "Andriy Lunin",
    "Fran González",
    "Sergio Mestre",
    "Dani Carvajal",
    "Álvaro Carreras",
    "Fran García",
    "Trent Alexander-Arnold",
    "Antonio Rüdiger",
    "Ferland Mendy",
    "David Alaba",
    "Éder Militão",
    "Jude Bellingham",
    "Eduardo Camavinga",
    "Federico Valverde",
    "Aurélien Tchouaméni",
    "Arda Güler",
    "Dani Ceballos",
    "Jude Bellingham",
    "Brahim Díaz",
    "Vinícius Júnior",
    "Endrick",
    "Kylian Mbappé",
    "Rodrygo",
    "Gonzalo García",
    "Franco Mastantuono"
]

for jugador in real_madrid_jugadores:
    numLetras = len(jugador)
    if jugador[0].lower() == jugador[len(jugador)-1]:
        print(jugador)