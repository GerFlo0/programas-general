#Constantes
BLOCK = {
    "lenght" : 0.39,
    "height" : 0.2
}
JOINT = {
    "lenght" : 0.01,
    "height" : 0.015
}

#Variables
wall = {
    "lenght" : float(input("Ingrese el ancho del muro: ")),
    "height" : float(input("Ingrese el alto del muro: "))
}

#Formula
wall_area = wall["lenght"] * wall["height"]

blocks_total = ( wall_area ) / ( (BLOCK["lenght"] + JOINT["lenght"]) * (BLOCK["height"] + JOINT["height"]) )


print(f"Para este muro de {wall_area} metros cuadrados se ocupan {blocks_total:.2f} blocks")

#datos de ejemplo 18 M de ancho por 2.7 de alto