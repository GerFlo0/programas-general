import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import re

# --- Constantes ---
RUTAS = {
    "Tijuana": {"KM": 2500, "L": 714},
    "Cd Juarez": {"KM": 1380, "L": 394},
    "Nuevo Laredo": {"KM": 720, "L": 206},
    "Puerto Vallarta": {"KM": 624, "L": 178},
    "Merida": {"KM": 1700, "L": 486},
    "Nogales": {"KM": 1720, "L": 491},
    "Tuxtla Gutierrez": {"KM": 1230, "L": 351},
    "Puerto Escondido": {"KM": 1050, "L": 300},
    "Manzanillo": {"KM": 615, "L": 176}
}

TANK = 500
COST_PER_L = 26
KM_PER_L = 3.5
WINDOW_SIZE = "900x400"
HEADERS = ["Autobús", "Destino", "Corridas"]

entradas = []

# --- Crear ventana principal ---
root = tk.Tk()
root.title("Registro de Corridas de Autobuses")
root.geometry(WINDOW_SIZE)
root.configure(bg="#f0f0f0")  # Fondo de ventana

# --- Cargar imagen ---
image_path = r"tec\\prog_logica_y_funcional\\src\\mex_map_2.png"
image = Image.open(image_path).resize((300, 250))  
photo = ImageTk.PhotoImage(image)

# --- Frames con estilos ---
frame_imagen = tk.Frame(root, width=320, height=260, bg="#d9d9d9", relief="ridge", borderwidth=2)
frame_imagen.place(x=20, y=20)

frame_formulario = tk.Frame(root, bg="#f0f0f0")
frame_formulario.place(x=350, y=20)

frame_tabla = tk.Frame(root, bg="#d9d9d9", relief="ridge", borderwidth=2)
frame_tabla.place(x=350, y=120, width=530, height=250)

# --- Mostrar imagen ---
label_imagen = tk.Label(frame_imagen, image=photo, bg="#d9d9d9")
label_imagen.image = photo
label_imagen.pack(expand=True)

# --- Opciones de autobuses y destinos ---
buses = ["Unidad 1", "Unidad 2", "Unidad 3", "Unidad 4", "Unidad 5"]
destinos = list(RUTAS.keys())

selected_bus = tk.StringVar(value="Seleccione")
selected_destino = tk.StringVar(value="Seleccione")

# --- Función para procesar la entrada ---
def procesar_entrada():
    try:
        corridas = entry_corridas.get()
        if not corridas.isdigit():  
            return
        
        unidad = selected_bus.get()
        destino = selected_destino.get()
        
        if unidad == "Seleccione" or destino == "Seleccione":
            return

        corridas = int(corridas)
        km = RUTAS[destino]["KM"] * corridas
        litros = km / KM_PER_L
        costo = litros * COST_PER_L
        tanques = litros / TANK

        # Agregar datos a la lista
        entradas.append([
            unidad, destino, corridas, f"{km:,.2f}", f"{litros:,.2f}",
            f"{costo:,.2f}", f"{tanques:,.2f}"
        ])

        # Limpiar selección
        selected_bus.set("Seleccione")
        selected_destino.set("Seleccione")
        entry_corridas.delete(0, tk.END)
    except:
        pass  

# --- Función para actualizar la tabla ---
def actualizar_tabla():
    tabla.delete(*tabla.get_children())  
    
    for index, fila in enumerate(entradas):
        color = "#e6f7ff" if index % 2 == 0 else "#ffffff"  
        tabla.insert("", tk.END, values=fila, tags=("evenrow" if index % 2 == 0 else "oddrow"))
    
    entradas.clear()

# --- Estilos de la tabla ---
style = ttk.Style()
style.configure("Treeview", background="#ffffff", foreground="black", rowheight=25, fieldbackground="#ffffff")
style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="#0078D7", foreground="white")
style.map("Treeview", background=[("selected", "#0078D7")])
style.configure("TButton", background="#0078D7", foreground="white", font=("Arial", 10, "bold"))

# --- Labels y Widgets del formulario ---
tk.Label(frame_formulario, text="Autobús", bg="#f0f0f0", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame_formulario, text="Destino", bg="#f0f0f0", font=("Arial", 10)).grid(row=0, column=1, padx=5, pady=5)
tk.Label(frame_formulario, text="Corridas", bg="#f0f0f0", font=("Arial", 10)).grid(row=0, column=2, padx=5, pady=5)

menu_buses = ttk.OptionMenu(frame_formulario, selected_bus, *["", *buses])
menu_buses.grid(row=1, column=0, padx=5, pady=5)

menu_destinos = ttk.OptionMenu(frame_formulario, selected_destino, *["", *destinos])
menu_destinos.grid(row=1, column=1, padx=5, pady=5)

entry_corridas = ttk.Entry(frame_formulario, width=5)
entry_corridas.grid(row=1, column=2, padx=5, pady=5)

btn_guardar = ttk.Button(frame_formulario, text="Guardar", command=procesar_entrada)
btn_guardar.grid(row=1, column=3, padx=5, pady=5)

btn_terminar = ttk.Button(frame_formulario, text="Terminar", command=actualizar_tabla)
btn_terminar.grid(row=1, column=4, padx=5, pady=5)

# --- Creación de tabla ---
columnas = ["unidad", "destino", "corridas", "km", "L", "costo", "tanques"]
tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

for col in columnas:
    tabla.heading(col, text=col.capitalize(), anchor="center")
    tabla.column(col, width=70, anchor="center")

tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# --- Agregar scrollbar ---
scrollbar = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# --- Agregar tags para filas de la tabla ---
tabla.tag_configure("evenrow", background="#e6f7ff")
tabla.tag_configure("oddrow", background="#ffffff")

# --- Ejecutar la aplicación ---
root.mainloop()
