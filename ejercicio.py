def obtener_calificaciones():
    while True:
        try:
            # Solicitar al usuario una lista de calificaciones separadas por comas
            entrada = input("Ingrese las calificaciones separadas por comas: ")
            
            # Dividir la cadena en calificaciones individuales
            calificaciones = entrada.split(',')
            
            # Inicializar una lista vacía para almacenar las calificaciones como enteros
            calificaciones_enteros = []
            
            # Convertir cada calificación en un entero y almacenarla en la lista
            for calificacion in calificaciones:
                calificacion_entero = int(calificacion.strip())
                calificaciones_enteros.append(calificacion_entero)
            
            return calificaciones_enteros
        except ValueError:
            print("Error: Ingrese calificaciones válidas separadas por comas.")

if __name__ == "__main__":
    calificaciones = obtener_calificaciones()
    print("Calificaciones ingresadas:", calificaciones)
