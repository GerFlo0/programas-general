#cuatro paredes
#pared 1 normal
#pared 2 y 3 una ventana cada una
#pared 4 una puerta
#medidas de la puerta 1 x 1.9 m
#ventanas largo 1.2m ancho 1.5ms
#Entradas
#ancho del frente
#lateral
#altura

#Constantes
BLOCK = {
    "lenght" : 0.39,
    "height" : 0.2
}
JOINT = {
    "lenght" : 0.01,
    "height" : 0.015
}
DOOR_AREA = (1 * 1.9)
WINDOW_AREA = (1.2 * 1.5)

#Variables
room = {
    "width" : float(input("Ingrese el ancho del frente: ")),
    "lenght" : float(input("Ingrese el ancho del lateral: ")),
    "height" : float(input("Ingrese la altura del cuarto: "))
}

#Formula
walls_area_no_holes = 2 * (room["width"] * room["height"]) + 2 * (room["lenght"] * room["height"])
walls_area = walls_area_no_holes - (DOOR_AREA + 2 * WINDOW_AREA)
blocks_total = ( walls_area ) / ( (BLOCK["lenght"] + JOINT["lenght"]) * (BLOCK["height"] + JOINT["height"]) )

print(f"Para este cuarto de {walls_area:.2f} metros cuadrados se ocupan {blocks_total:.2f} blocks")