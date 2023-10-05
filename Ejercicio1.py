def calcular_porcentaje(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        if y == 0:
            raise ZeroDivisionError
        if x < 0 or y < 0:
            raise ValueError
        if x <= y:
            percent = (x / y) * 100
            if percent < 1:
                return 'E'
            elif percent > 99:
                return 'F'
            else:
                return str(round(percent)) + '%'
        else:
            raise ValueError
    except ValueError:
        print("Error: Ingrese una fracción válida con números enteros, X debe ser menor o igual a Y y Y no puede ser igual a 0.")
        return None
    except ZeroDivisionError:
        print("Error: Y no puede ser igual a 0.")
        return None

while True:
    input_fraction = input("Ingrese una fracción en el formato X/Y (donde X e Y son enteros): ")
    result = calcular_porcentaje(input_fraction)
    if result is not None:
        print("Cantidad de combustible en el tanque:", result)
        break
