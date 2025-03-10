import os
import json


class Producto:
    """
    Representa un producto en el inventario de la tienda.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id_producto = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    def get_id_producto(self):
        return self._id_producto

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def to_dict(self):
        return {
            "id_producto": self._id_producto,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(data["id_producto"], data["nombre"], data["cantidad"], data["precio"])

    def __str__(self):
        return f"{self._nombre} (ID: {self._id_producto}) - Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"


class Inventario:
    """
    Gestiona los productos en la tienda.
    """
    ARCHIVO_INVENTARIO = "inventario.json"

    def __init__(self):
        self.productos = {}
        self.ids_existentes = set()
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        try:
            with open(self.ARCHIVO_INVENTARIO, "w") as archivo:
                json.dump([p.to_dict() for p in self.productos.values()], archivo, indent=4)
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")

    def cargar_desde_archivo(self):
        if os.path.exists(self.ARCHIVO_INVENTARIO):
            try:
                with open(self.ARCHIVO_INVENTARIO, "r") as archivo:
                    datos = json.load(archivo)
                    self.productos = {p["id_producto"]: Producto.from_dict(p) for p in datos}
                    self.ids_existentes = set(self.productos.keys())
            except (FileNotFoundError, json.JSONDecodeError):
                print("Advertencia: No se pudo leer el archivo de inventario o está vacío.")

    def agregar_producto(self, producto):
        if producto.get_id_producto() in self.productos:
            print("Error: El producto con este ID ya existe.")
        else:
            self.productos[producto.get_id_producto()] = producto
            self.ids_existentes.add(producto.get_id_producto())
            self.guardar_en_archivo()
            print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.ids_existentes.remove(id_producto)
            self.guardar_en_archivo()
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
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
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")


def obtener_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingresa un número entero válido.")


def obtener_flotante(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Ingresa un número válido.")


def menu():
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
            if id_producto in inventario.ids_existentes:
                print("Error: Este ID ya existe. Use otro.")
                continue
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = obtener_entero("Ingrese la cantidad del producto: ")
            precio = obtener_flotante("Ingrese el precio del producto: ")
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