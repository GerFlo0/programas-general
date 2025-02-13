#parametros
#4 varillas por columna
#anillo cada 10 cm

#entrada: numero de columnas y altura de los muros

#Salida: cuantas varillas ocupare, cuantos metros y cuantos anillos

#constantes
RING_SPACE = 0.1
ROD_PER_COLUMN = 4

#variables
columns = int(input("Cuantas columnas habrá?: "))
wall_height = float(input("Cual es la altura de los muros en metros?: "))

rod_amount = columns * ROD_PER_COLUMN
rod_meters = rod_amount * wall_height

ring_per_column = wall_height / RING_SPACE
ring_amount = ring_per_column * columns

#Salida
print(f"""Para esta construccion se ocuparan los siguientes materiales
    Varillas: {rod_amount}
    Metros de varillaa: {rod_meters:.2f}
    Cantidad de anillos: {ring_amount}""")