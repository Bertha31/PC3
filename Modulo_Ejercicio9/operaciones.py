# operaciones.py

def suma(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

def resta(a, b):
    try:
        resultado = a - b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

def multiplicacion(a, b):
    try:
        resultado = a * b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

def division(a, b):
    try:
        if b == 0:
            return "Error: No es posible dividir entre cero"
        resultado = a / b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

def ingreso_numero_decimal(msg:str = 'Ingrese un número decimal: ')->float:
    try:
        x = float(input(msg))
        return x
    except:
        return ingreso_numero_decimal(msg)