import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "Está sobre el origen"
        elif self.x == 0:
            return "Está sobre el eje Y"
        elif self.y == 0:
            return "Está sobre el eje X"
        elif self.x > 0 and self.y > 0:
            return "Cuadrante 1"
        elif self.x < 0 and self.y > 0:
            return "Cuadrante 2"
        elif self.x < 0 and self.y < 0:
            return "Cuadrante 3"
        elif self.x > 0 and self.y < 0:
            return "Cuadrante 4"
    
    def vector(self, otro_punto):
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        return Punto(dx, dy)
    
    def distancia(self, otro_punto):
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return distancia

class Rectangulo:
    def __init__(self, punto1=Punto(), punto2=Punto()):
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return abs(self.punto2.x - self.punto1.x)
    
    def altura(self):
        return abs(self.punto2.y - self.punto1.y)

    def area(self):
        return self.base() * self.altura()

# Ejemplo de uso:
p1 = Punto(2, 3)
p2 = Punto(5, 7)
rectangulo = Rectangulo(p1, p2)

print("Punto 1:", p1)
print("Punto 2:", p2)
print("Cuadrante de Punto 1:", p1.cuadrante())
print("Vector entre Punto 1 y Punto 2:", p1.vector(p2))
print("Distancia entre Punto 1 y Punto 2:", p1.distancia(p2))
print("Base del rectángulo:", rectangulo.base())
print("Altura del rectángulo:", rectangulo.altura())
print("Área del rectángulo:", rectangulo.area())
