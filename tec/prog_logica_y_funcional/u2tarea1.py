#calculo de distancias
#haciendo x numero de corridas a cada destino desde san luis, cuantos km recorre en total
# y cuantos litros de diesel se consumen en cada conjunto de corridas
#para el jueves 20 de febrero

import tkinter as tk
from PIL import Image, ImageTk

RUTAS = {
    "Tijuana": {"KM": 2500, "L": 714},
    "Cd Juarez": {"KM": 1380, "L": 394},
    "Nuevo Laredo": {"KM": 720, "L": 206},
    "Puerto Vallarta": {"KM": 624, "L": 178},
    "Merida": {"KM": 1700, "L": 486}}
TANK = 500
WINDOW_SIZE = "650x350"

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
label_imagen = tk.Label(frame_imagen, image=photo)
label_imagen.image = photo
label_imagen.place(relx=0.5, rely=0.5, anchor="center")

# Crear etiquetas y campos de entrada
lbls = {"routes": [], "entries":[], "results":[]}

for i, ruta in enumerate(RUTAS.keys()):
    lbls["routes"].append(tk.Label(root, text=ruta))
    lbls["routes"][i].place(x=250, y=50 + i * 30)
    
    lbls["entries"].append(tk.Entry(root, width=5))
    lbls["entries"][i].place(x=340, y=50 + i * 30)
    
    lbls["results"].append(tk.Label(root, text=""))
    lbls["results"][i].place(x=380, y=50 + i * 30)

# Función para calcular los resultados
def calc_results():
    for i, ruta in enumerate(RUTAS.keys()):
        try:
            entry = int(lbls["entries"][i].get())
            if entry < 0: raise ValueError
            if entry != 0:
                total_km = entry * RUTAS[ruta]["KM"]
                total_l = entry * RUTAS[ruta]["L"]
                lbls["results"][i].config(text=f"{total_km} km, {total_l} L")
        except ValueError:
            print(f"Error en campo '{ruta}'")

# Botón calcular
boton_calcular = tk.Button(root, text="CALCULAR")
boton_calcular.place(x=350, y=220)
boton_calcular.config(command=calc_results)

root.mainloop()