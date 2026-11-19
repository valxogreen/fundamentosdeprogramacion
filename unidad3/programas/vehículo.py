class Vehiculo:
    def __init__(self, marca, modelo, anio, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color

    def mostrar_caracteristicas(self):
        print("Marca: " , self.marca)
        print("Modelo: " ,self.modelo)
        print("Año: " , self.anio)
        print("Color: " , self.color)
