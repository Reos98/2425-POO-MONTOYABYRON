import os
import json

class Producto:
    """
    Representa un producto en el inventario de la tienda.
    """
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id_producto = id_producto  # Atributo privado para garantizar encapsulación
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id_producto(self):
        return self._id_producto

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def to_dict(self):
        """Convierte el objeto a un diccionario para facilitar el almacenamiento en archivos."""
        return {
            "id_producto": self._id_producto,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    @staticmethod
    def from_dict(data):
        """Crea un objeto Producto a partir de un diccionario."""
        return Producto(data["id_producto"], data["nombre"], data["cantidad"], data["precio"])

    def __str__(self):
        return f"{self._nombre} (ID: {self._id_producto}), Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"


class Inventario:
    """
    Gestiona los productos en la tienda, permitiendo agregar, eliminar, actualizar y buscar productos.
    """
    ARCHIVO_INVENTARIO = "inventario.txt"

    def __init__(self):
        self.productos = {}  # Diccionario con ID del producto como clave
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        """Guarda el inventario en un archivo de texto en formato JSON."""
        try:
            with open(self.ARCHIVO_INVENTARIO, "w") as archivo:
                json.dump([p.to_dict() for p in self.productos.values()], archivo)
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo de inventario.")

    def cargar_desde_archivo(self):
        """Carga los productos desde el archivo de inventario si existe."""
        if os.path.exists(self.ARCHIVO_INVENTARIO):
            try:
                with open(self.ARCHIVO_INVENTARIO, "r") as archivo:
                    datos = json.load(archivo)
                    self.productos = {p["id_producto"]: Producto.from_dict(p) for p in datos}
            except (FileNotFoundError, json.JSONDecodeError):
                print("Advertencia: No se pudo leer el archivo de inventario o está vacío.")

    def agregar_producto(self, producto):
        """Añade un producto al inventario si el ID es único."""
        if producto.get_id_producto() in self.productos:
            print("Error: El producto con este ID ya existe.")
        else:
            self.productos[producto.get_id_producto()] = producto
            self.guardar_en_archivo()
            print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario por su ID."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad o el precio de un producto por su ID."""
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            self.guardar_en_archivo()
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos por nombre."""
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")


def menu():
    """Interfaz de usuario en consola para gestionar el inventario."""
    inventario = Inventario()
    while True:
        print("\n=== Sistema de Gestión de Inventario ===")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '6':
            print("Saliendo del sistema...")
            break
        elif opcion == '1':
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            inventario.mostrar_inventario()
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()