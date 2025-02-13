#material para el techo de una casa

#constantes
#espesor del techo 0.1m
#para cada m3 de concreto se ocupa 350kg de cemento, 0.56m3 de arena, 0.84m3 de grava,  180 L de agua

#entradas
#ancho del frente
#ancho del lateral

#salida
#material para el techo

#Constantes
ROOF_HEIGHT = 0.1
MATERIALS_PER_CUB_METER = {
    "cement" : 350/50,
    "sand" : 0.56,
    "gravel" : 0.84,
    "water" : 180
}

#variables
roof = {
    "length" : float(input("Ingrese el ancho del cuarto: ")),
    "width" : float(input("Ingrese el frente del cuarto: "))
}

floor_area = roof["length"] * roof["width"]
floor_volume = floor_area * ROOF_HEIGHT

materials_total = {k: v*floor_volume for k,v in list(zip(MATERIALS_PER_CUB_METER.keys(), MATERIALS_PER_CUB_METER.values()))}

#salida

print(f"""Para este techo de {floor_area} metros cuadrados se necesitaran los siguientes materiales
    Cemento: {materials_total['cement']:.2f} bultos de 50kg ()
    Arena: {materials_total['sand']:.2f} metros cubicos
    Grava: {materials_total['gravel']:.2f} metros cubicos
    Agua: {materials_total['water']:.2f} litros""")