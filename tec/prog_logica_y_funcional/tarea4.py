#input: largo y ancho del cuarto
#constante espesor del piso en 0.15m
#para cada m3 de concreto se ocupa 350kg de cemento, 0.56m3 de arena, 0.84m3 de grava,  180 L de agua
#(concreto en sacos)

#ejemplos, largo: 9m, ancho: 6m, espesor: 15cm   8.1 m3
#ejemplo2, largo12 ancho8 esp0.18

#output, material para el piso

#Constantes
FLOOR_HEIGHT = 0.15
MATERIALS_PER_CUB_METER = {
    "cement" : 350/50,
    "sand" : 0.56,
    "gravel" : 0.84,
    "water" : 180
}

#variables
floor = {
    "length" : float(input("Ingrese el largo del piso: ")),
    "width" : float(input("Ingrese el ancho del piso: "))
}

floor_area = floor["length"] * floor["width"]
floor_volume = floor_area * FLOOR_HEIGHT

materials_total = {k: v*floor_volume for k,v in list(zip(MATERIALS_PER_CUB_METER.keys(), MATERIALS_PER_CUB_METER.values()))}

#salida
print(f"""Para este piso de {floor_area} metros cuadrados ({floor_volume} metros cubicos) se necesitaran los siguientes materiales
    Cemento: {materials_total['cement']:.2f} bultos de 50kg
    Arena: {materials_total['sand']:.2f} metros cubicos
    Grava: {materials_total['gravel']:.2f} metros cubicos
    Agua: {materials_total['water']:.2f} litros""")