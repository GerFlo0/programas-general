#Entradas largo (16) y alto de la pared(1.9)
#medidas de las ventanas (cada una de diferente tamaño)
#v1 1.5 * 1.2  v2 2.1 * 1.4

#Constantes
BLOCK_WIDTH = 0.39
BLOCK_HEIGHT = 0.2
JOINT_WIDTH = 0.01
JOINT_HEIGHT = 0.015

#Variables
wall = {
    "width" : float(input("Ingrese el ancho del muro: ")),
    "height" : float(input("Ingrese el alto del muro: "))
}

win_1 = {
    "width" : float(input("Ingrese el ancho de la ventana 1: ")),
    "height" : float(input("Ingrese el alto de la ventana 1: "))
}

win_2 = {
    "width" : float(input("Ingrese el ancho de la ventana 2: ")),
    "height" : float(input("Ingrese el alto de la ventana 2: "))
}

#Formula
area_wall = wall["width"] * wall["height"]
area_win_1 = win_1["width"] * win_1["height"]
area_win_2 = win_2["width"] * win_2["height"]

Cl = (area_wall - area_win_1 - area_win_2) / ( (BLOCK_WIDTH+JOINT_WIDTH) * (BLOCK_HEIGHT+JOINT_HEIGHT) )


print(f"Para este muro se ocupan {Cl:.2f} blocks")

#datos de ejemplo 18 M de ancho por 2.7 de alto