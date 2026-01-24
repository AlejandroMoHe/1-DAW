paises = [
    ["Argentina", "Buenos Aires", 46000000, "América", 2780400],  
    ["España", "Madrid", 48000000, "Europa", 505990],  
    ["Japón", "Tokio", 125000000, "Asia", 377975],  
    ["Sudáfrica", "Pretoria", 60000000, "África", 1221037],  
    ["Australia", "Canberra", 26000000, "Oceanía", 7692024],  
    ["Canadá", "Ottawa", 38000000, "América", 9984670]  
]

def masPobladoContinente(paises: list[list], continente: str) -> list:
    # Primero me quedo con los países del continente
    paisesContinente = [pais for pais in paises if pais[3] == continente]

    densidadMax = paisesContinente[0][2] / paisesContinente[0][4]
    for pais in paisesContinente