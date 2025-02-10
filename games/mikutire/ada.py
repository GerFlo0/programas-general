import math

pi = math.pi
ancho = float
relacion = float
diametro_llanta = float
radio = float
perimetro = float
ancho_cuerda = float
metros_perimetro = float
metros_cara = float

def fun_radio(diametro_llanta = float, relacion = float):
    return (5*diametro_llanta/math.sqrt(100-relacion)) * 10

def fun_perimetro(r):
    return (2*r)*pi

def fun_metros_perimetro(ancho = float, perimetro = float, ancho_cuerda = float):
    return (math.ceil(ancho/ancho_cuerda) * perimetro)

def fun_metros_cara(radio = float, ancho_cuerda = float, suma_perimetros = 0.0):
    
    if radio <= 0: return suma_perimetros
    
    suma_perimetros += fun_perimetro(radio)/1000
    
    return fun_metros_cara(radio - ancho_cuerda, ancho_cuerda, suma_perimetros)


ancho = float(input("Ancho del neumatico (milimetros): "))
relacion = float(input("Perfil del neumatico (porcentaje): "))
diametro_llanta = float(input("Radio de la llanta (pulgadas): "))*2.54
ancho_cuerda = float(input("Ancho de la cuerda (milimetros): "))

radio = fun_radio(diametro_llanta, relacion)
perimetro = fun_perimetro(radio)/1000

print(f"radio: {radio}")

metros_cara = fun_metros_cara(radio, ancho_cuerda)
metros_perimetro = fun_metros_perimetro(ancho, perimetro, ancho_cuerda)

print(f"metros cara: {metros_cara}")
print(f"metros perimetro: {metros_perimetro}")

print(f"Metros de cuerda totales requeridos: {metros_cara + metros_perimetro}")