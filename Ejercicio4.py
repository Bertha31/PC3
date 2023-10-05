class RECTANGULO:
    def __init__(self):
        self.largo = self.obtener_largo()
        self.ancho = self.obtener_ancho()

    def obtener_largo(self):
        while True:
            try:
                largo = float(input("Ingrese el largo del rectángulo: "))
                if largo >= 0:
                    return largo
                else:
                    print("El largo no puede ser negativo. Intente nuevamente.")
            except ValueError:
                print("El valor ingresado no es válido. Intente nuevamente.")

    def obtener_ancho(self):
        while True:
            try:
                ancho = float(input("Ingrese el ancho del rectángulo: "))
                if ancho >= 0:
                    return ancho
                else:
                    print("El ancho no puede ser negativo. Intente nuevamente.")
            except ValueError:
                print("El valor ingresado no es válido. Intente nuevamente.")

    def calcular_area(self):
        area = self.largo * self.ancho
        return area

area = RECTANGULO().calcular_area()
print(f"El área del rectángulo es: {area}")