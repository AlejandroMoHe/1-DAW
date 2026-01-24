planetas = [
    ["Mercurio", True, 2439.7],
    ["Venus", True, 6051.8],
    ["Tierra", True, 6371.0],
    ["Marte", True, 3389.5],
    ["Júpiter", False, 69911],
    ["Saturno", False, 58232],
    ["Urano", False, 25362],
    ["Neptuno", False, 24622],
    ["Plutón", True, 1188.3]  # Incluyendo a Plutón
]

for i, planeta in enumerate(planetas):
    for j, estado in enumerate(planeta):
        if estado == True:
            print(planeta)
