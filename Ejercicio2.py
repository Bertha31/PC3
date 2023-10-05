def obtener_calificaciones():
    while True:
        try:
            entrada = input("Ingrese las calificaciones separadas por comas: ")
            calificaciones = entrada.split(',')
            calificaciones_enteros = []
            for calificacion in calificaciones:
                calificacion_entero = int(calificacion.strip())
                calificaciones_enteros.append(calificacion_entero)
            return calificaciones_enteros
        except ValueError:
            print("Error: Ingrese calificaciones válidas separadas por comas.")

if __name__ == "__main__":
    calificaciones = obtener_calificaciones()
    print(f"Calificaciones ingresadas: {calificaciones}")