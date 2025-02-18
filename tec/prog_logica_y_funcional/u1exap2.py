#cuatro paredes
#pared 1, 2 y 3 una ventana cada una
#cada ventana de medidas diferentes
#pared 4 una puerta

#Entradas
#ancho del frente
#lateral
#altura
#medidas de cada ventana
#medidas de la puerta

#salida
#area de las paredes
#cantidad de blocks necesarios

import os
os.system('cls')

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
room = {
    "width" : float(input("Ingrese el ancho del frente: ")),
    "lenght" : float(input("Ingrese el ancho del lateral: ")),
    "height" : float(input("Ingrese la altura del cuarto: "))
}

holes = {
    "door" : {
        "width" : float(input("Ingrese el ancho de la puerta: ")),
        "height" : float(input("Ingrese la altura de la puerta: "))
    },
    "window1" : {
        "width" : float(input("Ingrese el ancho de la ventana izq: ")),
        "height" : float(input("Ingrese la altura de la ventana izq: "))
    },
    "window2" : {
        "width" : float(input("Ingrese el ancho de la ventana der: ")),
        "height" : float(input("Ingrese la altura de la ventana der: "))
    },
    "window3" : {
        "width" : float(input("Ingrese el ancho de la ventana tra: ")),
        "height" : float(input("Ingrese la altura de la ventana tra: "))
    }
}

#Formula
walls_area_no_holes = 2 * (room["width"] * room["height"]) + 2 * (room["lenght"] * room["height"])
holes_areas = {
    "door" : holes["door"]["width"] * holes["door"]["height"],
    "window1" : holes["window1"]["width"] * holes["window1"]["height"],
    "window2" : holes["window2"]["width"] * holes["window2"]["height"],
    "window3" : holes["window3"]["width"] * holes["window3"]["height"]
}
sum_holes_areas = sum(holes_areas.values())
walls_area = walls_area_no_holes - sum_holes_areas
blocks_total = ( walls_area ) / ( (BLOCK["lenght"] + JOINT["lenght"]) * (BLOCK["height"] + JOINT["height"]) )

print(f"Para este cuarto de {walls_area:.2f} metros cuadrados se ocupan {blocks_total:.2f} blocks")