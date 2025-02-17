import os
import msvcrt

#CONSTANTS
BLOCK = {
    "lenght" : 0.39,
    "height" : 0.2
}

JOINT = {
    "lenght" : 0.01,
    "height" : 0.015
}

RING_SPACE = 0.1

ROD_PER_COLUMN = 4

BLOCKS_PER_CUB_METER = 1 / ( (BLOCK["lenght"] + JOINT["lenght"]) * (BLOCK["height"] + JOINT["height"]) )

FLOOR_HEIGHT = 0.15

ROOF_HEIGHT = 0.1

DOOR_AREA = (1 * 1.9)

WINDOW_AREA = (1.2 * 1.5)

MATERIALS_PER_CUB_METER = {
    "cement" : 350/50,
    "sand" : 0.56,
    "gravel" : 0.84,
    "water" : 180
}

BLOCKS_PER_CUB_METER = 1 / ( (BLOCK["lenght"] + JOINT["lenght"]) * (BLOCK["height"] + JOINT["height"]) )

#FUNCTIONS

def area(x = 0, y = 0):
    return x * y

def volume( area = 0, height = 0):
    return area * height

def blocks( volume = 0):
    return volume * BLOCKS_PER_CUB_METER

def prog_1 ():
    wall = {
        "lenght" : float(input("Ingrese el ancho del muro: ")),
        "height" : float(input("Ingrese el alto del muro: "))
    }
    wall_area = area(wall["lenght"], wall["height"])
    blocks_total = blocks(wall_area)
    return f"\nPara este muro de {wall_area} metros cuadrados se ocupan {blocks_total:.2f} blocks"

def prog_2 ():
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
    area_wall = area(wall["width"], wall["height"])
    area_win_1 = area(win_1["width"], win_1["height"])
    area_win_2 = area(win_2["width"], win_2["height"])
    blocks_total = blocks( area_wall - area_win_1 - area_win_2 )
    return f"\npara este muro de {area_wall} metros cuadrados se necesitan {blocks_total:.2f} blocks"

def prog_3 ():
    columns = int(input("Cuantas columnas habrá?: "))
    wall_height = float(input("Cual es la altura de los muros en metros?: "))
    rod_amount = columns * ROD_PER_COLUMN
    rod_meters = rod_amount * wall_height
    ring_amount = (wall_height / RING_SPACE) * columns
    return f"""
    Para esta construccion se ocuparan los siguientes materiales
    Varillas: {rod_amount}
    Metros de varilla: {rod_meters:.2f}
    Cantidad de anillos: {ring_amount}"""

def prog_4 ():
    floor = {
        "length" : float(input("Ingrese el largo del piso: ")),
        "width" : float(input("Ingrese el ancho del piso: "))
    }
    floor_area = area(floor["length"], floor["width"])
    floor_volume = volume(floor_area, FLOOR_HEIGHT)
    materials_total = {k: v*floor_volume for k,v in list(zip(MATERIALS_PER_CUB_METER.keys(), MATERIALS_PER_CUB_METER.values()))}
    
    return f"""
    Para este piso de {floor_area} metros cuadrados ({floor_volume} metros cubicos) se necesitaran los siguientes materiales
    Cemento: {materials_total['cement']:.2f} bultos de 50kg ({(50 * materials_total['cement']):.2f} kg)
    Arena: {materials_total['sand']:.2f} metros cubicos
    Grava: {materials_total['gravel']:.2f} metros cubicos
    Agua: {materials_total['water']:.2f} litros"""

def prog_5 ():
    roof = {
        "length" : float(input("Ingrese el ancho del cuarto: ")),
        "width" : float(input("Ingrese el frente del cuarto: "))
    }
    floor_area = roof["length"] * roof["width"]
    floor_volume = floor_area * ROOF_HEIGHT
    materials_total = {k: v*floor_volume for k,v in list(zip(MATERIALS_PER_CUB_METER.keys(), MATERIALS_PER_CUB_METER.values()))}
    
    return f"""
    Para este techo de {floor_area} metros cuadrados se necesitaran los siguientes materiales
    Cemento: {materials_total['cement']:.2f} bultos de 50kg ({(50 * materials_total['cement']):.2f} kg)
    Arena: {materials_total['sand']:.2f} metros cubicos
    Grava: {materials_total['gravel']:.2f} metros cubicos
    Agua: {materials_total['water']:.2f} litros"""

def prog_6 ():
    room = {
        "front" : float(input("Ingrese el ancho del frente: ")),
        "side" : float(input("Ingrese el ancho del lateral: ")),
        "height" : float(input("Ingrese la altura del cuarto: "))
    }
    
    walls_area_no_holes = 2 * (room["front"] * room["height"]) + 2 * (room["side"] * room["height"])
    walls_area = walls_area_no_holes - (DOOR_AREA + 2 * WINDOW_AREA)
    blocks_total = blocks(walls_area)
    
    return f"\nPara este cuarto de {walls_area:.2f} metros cuadrados se ocupan {blocks_total:.2f} blocks"

def prog_7 ():
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
    holes_area = {
        "door" : holes["door"]["width"] * holes["door"]["height"],
        "window1" : holes["window1"]["width"] * holes["window1"]["height"],
        "window2" : holes["window2"]["width"] * holes["window2"]["height"],
        "window3" : holes["window3"]["width"] * holes["window3"]["height"]
    }
    sum_holes_area = sum(holes_area.values())
    walls_area = walls_area_no_holes - sum_holes_area
    blocks_total = ( walls_area ) / ( (BLOCK["lenght"] + JOINT["lenght"]) * (BLOCK["height"] + JOINT["height"]) )
    
    return(f"Para este cuarto de {walls_area:.2f} metros cuadrados se ocupan {blocks_total:.2f} blocks")

def menu():
    print("""\n---------------------------
|PROGRAMAS DE CONSTRUCCIÓN|
---------------------------
    1. Muro
    2. Muro con ventanas
    3. Columnas
    4. Piso
    5. Techo
    6. Cuarto
    7. Cuarto+
    8. Salir
    """)

def execute_option(option):
    options = {
        "1": prog_1,
        "2": prog_2,
        "3": prog_3,
        "4": prog_4,
        "5": prog_5,
        "6": prog_6,
        "7": prog_7
    }
    
    if option in options:
        print(options[option]())
    elif option == "8":
        return False
    else:
        print("Opción no válida")
    return True

#MAIN
while True:
    os.system('cls')
    menu()
    option = input("Seleccione una opción: ")
    if not execute_option(option):
        break
    print("\nPresione cualquier tecla para continuar...")
    msvcrt.getch()