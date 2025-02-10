import time

#declarar variables

x = 123
y = 20


palabra1 = "hamster"
palabra2 = "rojo"


z = x+y


palabra3 = palabra1+" "+palabra2




#almacenar datos por teclado en variables

var1 = input("cual es tu nombre?")




#mostrar texto

print("texto excrito desde codigo")


print(var1+": capturado por teclado")


print(z)

#modificar variable
z = 100

print(z)


print(palabra3)




#operadores de comparacion

#mayor que: >
#menor que: <
#igual que ==
#diferente que !=


#operadores logicos

# and
# or
# not


#estructuras de control

#espera

print("1")
time.sleep(1)


print("2")
time.sleep(3)


#comparacion

if(x>50):
    print("el numero es mayor que 50")


if(y<40):
    print("el numero es menor que 40")


if(z==143):
    print("se cumplio la condicion")
else:
    print("no se cumplio la condicion")



#repeticion por numero de veces

for i in range(3):
    print("este ciclo se repite tres veces")


for i in range(7):
    print("este ciclo se repite siete veces")



#repeticion por condicion

while(z>90):
    print("z")
    z -= 1

#!!!peligro!!!
#while(True):
#    print("A")