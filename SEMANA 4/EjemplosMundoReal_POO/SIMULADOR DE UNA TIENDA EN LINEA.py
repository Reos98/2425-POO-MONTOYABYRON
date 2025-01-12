class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

# Ejemplo de uso:
camiseta = Producto("Camiseta", 19.99, 10)
pantalon = Producto("Pantalón", 29.99, 5)

carrito = Carrito()
carrito.agregar_producto(camiseta)
carrito.agregar_producto(pantalon)

print("Total de la compra:", carrito.calcular_total())