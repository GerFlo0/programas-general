#calculo de distancias
#haciendo x numero de corridas a cada destino desde san luis, cuantos km recorre en total
# y cuantos litros de diesel se consumen en cada conjunto de corridas
#para el jueves 20 de febrero

import tkinter as tk
from tkinter import Entry, Label, Button
from PIL import Image, ImageTk

RUTAS = {
    "Tijuana": {"KM": 2500, "L": 714},
    "Cd Juarez": {"KM": 1380, "L": 394},
    "Nuevo Laredo": {"KM": 720, "L": 206},
    "Puerto Vallarta": {"KM": 624, "L": 178},
    "Merida": {"KM": 1700, "L": 486}
}
L_PER_KM = 3.5
TANK = 500
WINDOW_SIZE = "600x350"

# Crear la ventana principal
root = tk.Tk()
root.title("Corridas de autobuses")
root.geometry(WINDOW_SIZE)

# Crear un marco para la imagen
frame_imagen = tk.Frame(root, width=300, height=250)
frame_imagen.place(x=20, y=50)

# Cargar la imagen con PIL
image_path = r"tec\\prog_logica_y_funcional\\src\\mex_map.png"
image = Image.open(image_path)
image = image.resize((300, 250))  # Ajustar tamaño de la imagen
photo = ImageTk.PhotoImage(image)

# Crear Label para mostrar la imagen
label_imagen = Label(frame_imagen, image=photo)
label_imagen.image = photo  # Mantener referencia para evitar que la imagen se elimine
label_imagen.place(relx=0.5, rely=0.5, anchor="center")

# Crear etiquetas y campos de entrada
lbls = {"routes": [], "entries":[], "results":[],}

#setup de etiquetas, campos de entrada y resultados
for i, ruta in enumerate(RUTAS.keys()):
    lbls["routes"].append(Label(root, text=f"SLP a {ruta}"))
    lbls["routes"][i].place(x=250, y=50 + i * 30)
    
    lbls["entries"].append(Entry(root, width=5))
    lbls["entries"][i].place(x=370, y=50 + i * 30)
    
    lbls["results"].append(Label(root, text="..."))
    lbls["results"][i].place(x=430, y=50 + i * 30)

# Función para calcular los resultados
def calc_results():
    for i, ruta in enumerate(RUTAS.keys()):
        try:
            total_km = int(lbls["entries"][i].get()) * RUTAS[ruta]["KM"]
            total_l = int(lbls["entries"][i].get()) * RUTAS[ruta]["L"]
            total_t = total_l / TANK
            lbls["results"][i].config(text=f"{total_km} km, {total_l} L, {total_t} T")
        except ValueError:
            print(f"Error en campo '{ruta}'")

# Botón calcular
boton_calcular = Button(root, text="CALCULAR")
boton_calcular.place(x=350, y=220)
boton_calcular.config(command=calc_results)

root.mainloop()