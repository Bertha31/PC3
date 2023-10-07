

from utils import ingreso_datos as ing
from utils.circulo import calcular_area_circulo
from utils.rectangulo import calcular_area_rectangulo
from utils.cuadrado import calcular_area_cuadrado

MENSAJE_BIENVENIDA = "Bienvenido al menú interactivo"
OPCIONES_MENU = """
¿Qué quieres hacer? 
    1. Calcular el área de un circulo
    2. Calcular el área de un rectangulo
    3. Calcular el área de un cuadrado
    4. Salir

Escribe una opción: """


def opcion1():
    while True:
        radio = ing.ingreso_numero_decimal("Ingrese radio: ")
        if radio >=0:
            area = calcular_area_circulo(radio)
            print(f"El área del círculo es: {area}")
            break
        else:
            print ("Error. El radio debe ser positivo")


    
def opcion2():
    while True:
        largo = ing.ingreso_numero_decimal("Ingresa el largo del rectángulo: ")
        ancho = ing.ingreso_numero_decimal("Ingresa el ancho del rectángulo: ")
        if largo < 0 or ancho < 0:
            print("El largo y el ancho deben ser valores positivos. Por favor, inténtalo nuevamente.")
        else:
            break
    area = calcular_area_rectangulo(largo,ancho)
    print(f"El área del rectángulo es: {area}")

def opcion3():
    while True:
        lado = ing.ingreso_numero_decimal("Ingrese el lado del cuadrado: ")
        if lado >=0:
            area = calcular_area_cuadrado(lado)
            print(f"El área del cuadrado es: {area}")
            break
        else:
            print ("Error. El lado debe ser positivo")


def main():
    print(MENSAJE_BIENVENIDA)
    while True:
        opcion = input(OPCIONES_MENU)
        if opcion == '1':
            opcion1()
        elif opcion == '2':
            opcion2()
        elif opcion == '3':
            opcion3()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Vuelve a intentarlo, dígito erróneo")
    pass

if __name__ == '__main__':
    main()