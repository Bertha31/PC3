"""
Crear un programa Menu que contenga las siguientes funcionalidades:
1. Calcular el área de un circulo
2. Calcular el área de un rectangulo
3. Calcular el área de un cuadrado
4. Salir
"""

from pprint import pprint

from utils import ingreso_datos as ing
from utils.circulo import calcular_area_circulo
from utils.rectangulo import calcular_area_rectangulo
from utils.cuadrado import calcular_area_cuadrado

# 2. Constantes
MENSAJE_BIENVENIDA = "Bienvenido al menú interactivo"
OPCIONES_MENU = """
¿Qué quieres hacer? 
    1. Calcular el área de un circulo
    2. Calcular el área de un rectangulo
    3. Calcular el área de un cuadrado
    4. Salir

Escribe una opción: """


# 3. Funciones y /o metodos

def opcion1():
    while True:
        try:
            radio = float(input("Ingrese radio: "))
            if radio >=0:
                area = calcular_area_circulo()
                print(f"El área del círculo es: {area}")
                break
            else:
                print ("Error. El radio debe ser positivo")
        except ValueError:
            print("Error de digitación")

    
def opcion2():
    largo = ing.ingreso_numero_decimal('Ingrese el largo: ')
    ancho = ing.ingreso_numero_decimal('Ingrese el ancho: ')
    calcular_rectangulo = calcular_area_rectangulo(largo,ancho)
    print(f"El área del rectangulo es: {calcular_rectangulo}")


def opcion3():
    lado = ing.ingreso_numero_decimal('Ingrese el lado del cuadrado: ')
    calcular_cuadrado = calcular_area_cuadrado(lado)
    print(f"El área del cuadrado es: {calcular_cuadrado}")


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
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")
    pass

if __name__ == '__main__':
    main()