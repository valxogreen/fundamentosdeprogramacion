calificacion = float(input("Ingrese la calificación: "))
if calificacion > 10:
    print("calificacion invalida")
elif calificacion >= 9:
    print("Excelente")
elif calificacion > 8:
    print("buen trabajo")
elif calificacion < 0:
    print("calificacion invalida")
elif calificacion >= 6:
    print("Aprobado")
else:
    print("Reprobado")
