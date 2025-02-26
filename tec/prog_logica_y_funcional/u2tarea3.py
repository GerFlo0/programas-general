#agregar 4 ciudades más a la lista de rutas
#sonora, tuxcla gutierrez, puerto escondido, manzanillo colima

import tkinter as tk
from PIL import Image, ImageTk
km_por_litro = 3.5
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
WINDOW_SIZE = "750x350"

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
lbls = {
    "headers": {
        "ruta": tk.Label(root, text="Ruta"),
        "corridas": tk.Label(root, text="Corridas"),
        "km": tk.Label(root, text="Km"),
        "L": tk.Label(root, text="L"),
        "cost": tk.Label(root, text="Costo"),
        "tanks": tk.Label(root, text="Tanques")
        },
    "routes": [], 
    "entries":[], 
    "results":{
        "km": [],
        "L": [],
        "cost": [],
        "tanks": [],
        },
    "totals":{
        "km": tk.Label(root, text=""),
        "L": tk.Label(root, text=""),
        "cost": tk.Label(root, text=""),
        "tanks": tk.Label(root, text="")
        }
    }

for i, header in enumerate(lbls["headers"].keys()):
    lbls["headers"][header].place(x=340+i*65, y=20)

for i, ruta in enumerate(RUTAS.keys()):
    lbls["routes"].append(tk.Label(root, text=ruta))
    lbls["entries"].append(tk.Entry(root, width=3))
    lbls["results"]["km"].append(tk.Label(root, text=""))
    lbls["results"]["L"].append(tk.Label(root, text=""))
    lbls["results"]["cost"].append(tk.Label(root, text=""))
    lbls["results"]["tanks"].append(tk.Label(root, text=""))
    
    lbls["routes"][i].place(x=330, y=50+i*30)
    lbls["entries"][i].place(x=420, y=50+i*30)
    lbls["results"]["km"][i].place(x=460, y=50+i*30)
    lbls["results"]["L"][i].place(x=530, y=50+i*30)
    lbls["results"]["cost"][i].place(x=600, y=50+i*30)
    lbls["results"]["tanks"][i].place(x=670, y=50+i*30)
    
    if(i == len(RUTAS.keys())-1): patata = 50+i*30

for i in range(len(lbls["totals"].keys())):
    lbls["totals"][list(lbls["totals"].keys())[i]].place(x=460+i*70, y=patata+30)

# Función para calcular los resultados
def calc_results():
    tkm = 0
    tl = 0
    tcost = 0
    tt = 0
    for i, ruta in enumerate(RUTAS.keys()):
        corridas = int(lbls["entries"][i].get())
        km = corridas * RUTAS[ruta]["KM"]
        l = corridas * RUTAS[ruta]["L"]
        cost = l * COST_PER_L
        tanks = l / TANK
        tkm += km
        tl += l
        tcost += cost
        tt += tanks
        lbls["results"]["km"][i].config(text=f"{km:,.2f}")
        lbls["results"]["L"][i].config(text=f"{l:,.2f}")
        lbls["results"]["cost"][i].config(text=f"${cost:,.2f}")
        lbls["results"]["tanks"][i].config(text=f"{tanks:,.2f}")
    lbls["totals"]["km"].config(text=f"{tkm:,.2f}")
    lbls["totals"]["L"].config(text=f"{tl:,.2f}")
    lbls["totals"]["cost"].config(text=f"${tcost:,.2f}")
    lbls["totals"]["tanks"].config(text=f"{tt:,.2f}")

# Botón calcular
boton_calcular = tk.Button(root, text="CALCULAR")
boton_calcular.place(x=150, y=300)
boton_calcular.config(command=calc_results)

root.mainloop()