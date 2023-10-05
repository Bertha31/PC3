class CIRCULO:
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        area_circulo = 3.16 * self.radio**2
        return area_circulo

while True:
    try:
        radio_del_circulo = float(input("Ingrese radio: "))
        if radio_del_circulo>=0:
            area = CIRCULO(radio_del_circulo).calcular_area()
            print(f"El área del círculo es: {area}")
            break
        else:
            print ("Error. El radio debe ser positivo")
    except ValueError:
        print("Error de digitación")