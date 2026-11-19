import math 
class figura:
     def area(self):
         return 0

class rectangulo(figura):
     def __init__(self, base, altura):
              self.base = base
              self.altura = altura

     def area(self):
             return self.base * self.altura

class circulo(figura):
     def __init__(self, radio):
        self.radio = radio

     def area(self):
        return math.pi * (self.radio ** 2)    

class triangulo(figura):
     def __init__(self, base, altura):
        self.base = base
        self.altura = altura

     def area(self):
        return (self.base * self.altura) / 2    

figuras = [rectangulo(5, 10), circulo(7), triangulo(4, 6)]
for figura in figuras:
     print(type(figura).__name__, "Área:", round(figura.area(), 2)) 
