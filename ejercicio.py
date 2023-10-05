class RECTANGULO:
    def __init__(self, largo, ancho):
        if self.largo>=0 and self.ancho>=0:
            self.largo = largo
            self.ancho = ancho
        
    def calcular_area(self):
        area_rectangulo = self.largo * self.ancho
        return area_rectangulo
while True:
    try:
        largo_rectangulo = float(input("Ingrese largo: "))
        if largo_rectangulo>=0:
            pass
        else:
            print ("Error. El largo debe ser positivo")
    except ValueError:
        print("Error de digitación")     

    try:
        ancho_rectangulo = float(input("Ingrese ancho: "))
        if ancho_rectangulo>=0:
            area = RECTANGULO(largo_rectangulo,ancho_rectangulo).calcular_area()
            print(f"El área del círculo es: {area}")
            break 
        else:
            print ("Error. El largo debe ser positivo") 
    except ValueError:
        print("Error de digitación")    