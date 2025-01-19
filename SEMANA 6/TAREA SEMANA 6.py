class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = 0

    def agregar_stock(self, cantidad):
        self.__stock += cantidad

    def quitar_stock(self, cantidad):
        if self.__stock >= cantidad:
            self.__stock -= cantidad
        else:
            print("Stock insuficiente")

class Libro(Producto):
    def __init__(self, nombre, precio, autor, isbn, genero):
        super().__init__(nombre, precio)
        self.__autor = autor
        self.__isbn = isbn
        self.__genero = genero

class Ropa(Producto):
    def __init__(self, nombre, precio, talla, color, material):
        super().__init__(nombre, precio)
        self.__talla = talla
        self.__color = color
        self.__material = material

# Ejemplo de uso
libro1 = Libro("El Quijote", 20, "Miguel de Cervantes", "1234567890", "Novela")
camiseta = Ropa("Camiseta algodón", 15, "M", "Blanco", "Algodón")

libro1.agregar_stock(10)
camiseta.quitar_stock(5)