class Producto:
    # Constructor de clase
    def __init__(self, codigo,nombre,precio,anio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.anio = anio
        print('Se ha creado el producto:', self.nombre)

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}, Año: {self.anio}"
    pass


class Catalogo:

    productos = []  # Esta lista contendrá objetos de la clase Pelicula

    def __init__(self, productos=[]):
        self.productos = productos

    def agregar(self, p):  # p será un objeto Pelicula
        self.productos.append(p)

    def mostrar(self):
        for p in self.productos:
            print(p)  # Print toma por defecto str(p)


    def filtrar_por_anio(self, anio):
        productos_filtrados = [p for p in self.productos if p.anio == anio]
        if productos_filtrados:
            print(f"Productos para el año {anio}:")
            for p in productos_filtrados:
                print(p)
        else:
            print(f"No hay productos disponibles para el año {anio}")


# Ejemplo de uso:
if __name__ == "__main__":
    catalogo = Catalogo()

    producto1 = Producto("001", "Filtro de aceite", 15.99, 2022)
    producto2 = Producto("002", "Batería", 79.99, 2023)
    producto3 = Producto("003", "Pastillas de freno", 29.99, 2022)

    catalogo.agregar(producto1)
    catalogo.agregar(producto2)
    catalogo.agregar(producto3)

    print("Lista de todos los productos en el catálogo:")
    catalogo.mostrar()

    catalogo.filtrar_por_anio(2022)