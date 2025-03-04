#programa que registra la cantidad de corridas a un destino de cada unidad de autobuses de una empresa
#se deben usar listas desplegables para seleccionar el autobus y el destino
#para la cantidad de corridas un entry
#tras capturar todos los datos y presionar un boton dedicado, mostrar una tabla con los siguientes datos de cada entrada
#unidad, destino, cantidad de corridas, km totales, litros de gasolina, costo de gasolina, cantidad de tanques de gasolina

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import re
#constantes
RUTAS = {
    "Tijuana": {"KM": 2500, "L": 714},
    "Cd Juarez": {"KM": 1380, "L": 394},
    "Nuevo Laredo": {"KM": 720, "L": 206},
    "Puerto Vallarta": {"KM": 624, "L": 178},
    "Merida": {"KM": 1700, "L": 486},
    "Nogales": {"KM": 1720, "L": 491},
    "Tuxtla Gutierrez": {"KM": 1230, "L": 351},
    "Puerto Escondido": {"KM": 1050, "L": 300},
    "Manzanillo": {"KM": 615, "L": 176}}
TANK = 500
COST_PER_L = 26
KM_PER_L = 3.5
WINDOW_SIZE = "850x350"
HEADERS = ["Autobuses","Destinos", "Corridas"]

entradas = []

# Crear la ventana principal
root = tk.Tk()
root.geometry(WINDOW_SIZE)

# Crear un marco para la imagen
frame_imagen = tk.Frame(root, width=300, height=250)
frame_imagen.place(x=20, y=50)

frame = tk.Frame(root)
frame.place(x=350,y=100)
# Crear el Treeview
tabla = ttk.Treeview(frame, columns=("unidad", "destino", "corridas", "km", "L", "costo", "tanques"), show="headings")

# Configurar las columnas
tabla.heading("unidad", text="Unidad",anchor="center")
tabla.heading("destino", text="Destino",anchor="center")
tabla.heading("corridas", text="Corridas",anchor="center")
tabla.heading("km", text="Km",anchor="center")
tabla.heading("L", text="L",anchor="center")
tabla.heading("costo", text="Costo",anchor="center")
tabla.heading("tanques", text="Tanques",anchor="center")

tabla.column("unidad",width=60,anchor="center")
tabla.column("destino",width=100,anchor="center")
tabla.column("corridas",width=65,anchor="center")
tabla.column("km",width=60,anchor="center")
tabla.column("L",width=60,anchor="center")
tabla.column("costo",width=60,anchor="center")
tabla.column("tanques",width=60,anchor="center")

# Crear el Scrollbar
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscrollcommand=scrollbar.set)

# Ubicar el Treeview y el Scrollbar en el frame
tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Cargar la imagen con PIL
image_path = r"tec\\prog_logica_y_funcional\\src\\mex_map_2.png"
image = Image.open(image_path)
image = image.resize((300, 250))  # Ajustar tamaño de la imagen
photo = ImageTk.PhotoImage(image)

# Crear Label para mostrar la imagen
label_imagen = tk.Label(frame_imagen, image=photo)
label_imagen.image = photo
label_imagen.place(relx=0.5, rely=0.5, anchor="center")

# Crear una lista de autobuses y destinos
buses = ["Unidad 1", "Unidad 2", "Unidad 3", "Unidad 4", "Unidad 5"]
destinos = list(RUTAS.keys())

# Crear una variable para almacenar la opción seleccionada y el destino
selected_bus = tk.StringVar()
selected_destino = tk.StringVar()
selected_bus.set("Seleccione")  # Establecer un valor por defecto
selected_destino.set("Seleccione")  # Establecer un valor por defecto

def procesar_entrada():
    try:
        if(not re.search(r'\.',entry_corridas.get())):
            unidad = selected_bus.get()
            destino = selected_destino.get()
            if unidad  == "Seleccione"  or destino == "Seleccione": return None
            corridas = int(entry_corridas.get())
            km = RUTAS[destino]["KM"]*corridas
            l = km/KM_PER_L
            costo = l*COST_PER_L
            tanques = l/TANK
            
            entradas.append([unidad,destino,corridas,f"{km:,.2f}",f"{l:,.2f}",f"{costo:,.2f}",f"{tanques:,.2f}"])
            
            selected_bus.set("Seleccione")
            selected_destino.set("Seleccione")
            entry_corridas.delete(0, tk.END) 
    except: None

def terminar():
    for fila in tabla.get_children(): tabla.delete(fila)
    
    for fila in entradas: tabla.insert("", tk.END, values=fila)
    
    entradas.clear()

#crear cabecera
header = [tk.Label(root) for i in range(len(HEADERS))]

for i in range(len(header)): header[i].config(text=HEADERS[i])

header[0].place(x=350,y=30)
header[1].place(x=440,y=30)
header[2].place(x=570,y=30)

#crear entry para capturar la cantidad de corridas
entry_corridas = ttk.Entry(root)

# Crear los OptionMenu
menu_buses = ttk.OptionMenu(root, selected_bus, *["",*buses])
menu_destinos = ttk.OptionMenu(root, selected_destino, *["",*destinos])

# Botón para mostrar la opción seleccionada
btn_guardar = ttk.Button(root, text="Guardar entrada", command=procesar_entrada)

btn_terminar = ttk.Button(root, text="Terminar", command=terminar)

menu_buses.place(x=350,y=50)
menu_destinos.place(x=440,y=50)
entry_corridas.place(x=570,y=50,width=50)
btn_guardar.place(x=630,y=50)
btn_terminar.place(x=730,y=50)

# Iniciar el bucle principal de la ventana
root.mainloop()
