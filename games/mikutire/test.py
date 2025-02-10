import math
import tkinter as tk
from tkinter import messagebox

# Funciones
def fun_radio(diametro_llanta, relacion):
    return (5 * diametro_llanta / math.sqrt(100 - relacion)) * 10

def fun_perimetro(r):
    return (2 * r) * math.pi

def fun_metros_perimetro(ancho, perimetro, ancho_cuerda):
    return (math.ceil(ancho / ancho_cuerda) * perimetro)

def fun_metros_cara(radio, ancho_cuerda, suma_perimetros=0.0):
    if radio <= 0:
        return suma_perimetros
    suma_perimetros += fun_perimetro(radio) / 1000
    return fun_metros_cara(radio - ancho_cuerda, ancho_cuerda, suma_perimetros)

def calcular():
    try:
        # Obtener valores de entrada
        ancho = float(entry_ancho.get())
        relacion = float(entry_relacion.get())
        diametro_llanta = float(entry_diametro.get()) * 2.54  # Convertir pulgadas a milímetros
        ancho_cuerda = float(entry_ancho_cuerda.get())
        
        # Cálculos
        radio = fun_radio(diametro_llanta, relacion)
        perimetro = fun_perimetro(radio) / 1000
        metros_cara = fun_metros_cara(radio, ancho_cuerda)
        metros_perimetro = fun_metros_perimetro(ancho, perimetro, ancho_cuerda)
        total_cuerda = metros_cara + metros_perimetro

        # Mostrar resultado
        messagebox.showinfo("Resultado", f"Metros de cuerda totales requeridos: {total_cuerda:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Calculadora de Metros de Cuerda")

# Labels y entradas
tk.Label(root, text="Ancho del neumático (mm):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_ancho = tk.Entry(root)
entry_ancho.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Perfil del neumático (%):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_relacion = tk.Entry(root)
entry_relacion.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Diámetro de la llanta (pulgadas):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_diametro = tk.Entry(root)
entry_diametro.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Ancho de la cuerda (mm):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_ancho_cuerda = tk.Entry(root)
entry_ancho_cuerda.grid(row=3, column=1, padx=10, pady=5)

# Botón para calcular
tk.Button(root, text="Calcular", command=calcular).grid(row=4, column=0, columnspan=2, pady=10)

# Inicia el bucle principal de la interfaz
root.mainloop()
