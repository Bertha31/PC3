"""
Crear un programa Menu que contenga las siguientes funcionalidades:
1. Calcular el área de un circulo
2. Calcular el área de un rectangulo
3. Calcular el área de un cuadrado
4. Salir
"""

# 1. Librerias
from pprint import pprint


# 1.2 librerias creadas
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
    x = ing.ingreso_numero_decimal('Ingrese el primeor número: ')
    calcular_circulo= calcular_area_circulo(x)
    print(calcular_circulo)


def opcion2():
    x = ing.ingreso_numero_decimal('Ingrese el primeor número: ')
    y = ing.ingreso_numero_decimal('Ingrese el segundo número: ')
    calcular_rectangulo = calcular_area_rectangulo(x,y)
    print(calcular_rectangulo)


def opcion3():
    x = ing.ingreso_numero_decimal('Ingrese el primeor número: ')
    calcular_cuadrado = calcular_area_cuadrado(x)
    print(calcular_cuadrado)


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