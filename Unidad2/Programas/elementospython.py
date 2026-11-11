nombre = "Ana" 
edad = 19
estatura = 1.65
es_estudiante = True
#imprimir la variable y su tipo 
print("Nombre: ", nombre, type(nombre))
print("Edad:", edad, type(edad))
print("estatura:", estatura, type(estatura))
print("Estudiante:", es_estudiante, type(es_estudiante))


#declarar una constante
PROMEDIO_MINIMO = 6

#introducimos datos y los guardamos en variables materia y calificacion
materia = input("Que materia cursas?")
calificacion = float(input("¿Cuál es tu calificación?"))

#hacemos las operaciones basicas
suma = 8 + 2
resta = 10 % 3
potencia = 2 ** 3

#estamos declarando dos variables booleanas
mayor_de_edad = edad >= 18
aprobado = calificacion >= PROMEDIO_MINIMO and es_estudiante

#imprimimos el resultado 
print("suma:", suma, "resta:", resta, "potencia:", potencia)
print("Mayor de edad:", mayor_de_edad)

