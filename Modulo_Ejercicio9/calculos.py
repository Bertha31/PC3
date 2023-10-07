
import operaciones

a= operaciones.ingreso_numero_decimal("Ingrese el primer numero: ")
b =operaciones.ingreso_numero_decimal("Ingrese el segundo numero: ")


resultado_suma = operaciones.suma(a, b)
print(f"Suma: {resultado_suma}")

resultado_resta = operaciones.resta(a, b)
print(f"Resta: {resultado_resta}")

resultado_multiplicacion = operaciones.multiplicacion(a, b)
print(f"Multiplicación: {resultado_multiplicacion}")

resultado_division = operaciones.division(a, b)
print(f"División: {resultado_division}")
