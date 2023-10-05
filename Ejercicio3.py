class CIRCULO:
    def __int__ (self,radio)-> None:
        self.radio = radio
        pass
    def calcular_area(self):
        if self.radio >= 0:
            return 3.16*self.radio**2
        else:
            return "El radio está mal digitado"

numero_radio = float(input("Ingrese el radio: "))
print(calcular_area)   