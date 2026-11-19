import math

radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * math.pow(radio, 2)
perimetro = 2 * math.pi * radio

print("Area", round(area, 2))
print("Perímetro", round(perimetro, 2))
print("Raiz cuadrada del radio", round(math.sqrt(radio), 2))
print("Techo del area", math.ceil(area))

x=3 
y=4
pow = math.pow(x, y)
print("x, y", pow)

j=6
v=3
math = math.fmod(j, v)
print("j, v", math)

#la linea 1 esta importando la libreria math que nos permite realizar operaciones matemáticas como caclular#
#el valor de diversas funciones matematicass#



