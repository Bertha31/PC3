class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Nombre:", self.nombre)
        print("Número de Registro:", self.numero_registro)
        print("Edad:", self.edad)
        print("Notas:", self.notas)

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, nota):
        self.notas.append(nota)

# Ejemplo de uso:
alumno1 = Alumno("Juan Perez", 12345)
alumno1.setAge(20)
alumno1.setNota(90)
alumno1.setNota(85)

alumno1.display()
