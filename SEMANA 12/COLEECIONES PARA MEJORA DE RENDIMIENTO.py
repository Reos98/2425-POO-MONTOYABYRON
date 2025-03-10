import json

class Libro:
    def __init__(self, isbn, titulo, autor, categoria, prestado=False):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.prestado = prestado

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "prestado": self.prestado
        }

class Biblioteca:
    def __init__(self, archivo_json='biblioteca.json', archivo_usuarios='usuarios.json', archivo_prestamos='prestamos.json'):
        self.archivo_json = archivo_json
        self.archivo_usuarios = archivo_usuarios
        self.archivo_prestamos = archivo_prestamos
        self.libros = self.cargar_libros()
        self.usuarios_registrados = self.cargar_usuarios()
        self.libros_prestados = self.cargar_prestamos()

    def cargar_libros(self):
        try:
            with open(self.archivo_json, 'r') as archivo:
                datos_libros = json.load(archivo)
                return {isbn: Libro(**datos) for isbn, datos in datos_libros.items()}
        except FileNotFoundError:
            return {}

    def guardar_libros(self):
        with open(self.archivo_json, 'w') as archivo:
            json.dump({isbn: libro.to_dict() for isbn, libro in self.libros.items()}, archivo, indent=4)

    def cargar_usuarios(self):
        try:
            with open(self.archivo_usuarios, 'r') as archivo:
                return set(json.load(archivo))
        except FileNotFoundError:
            return set()

    def guardar_usuarios(self):
        with open(self.archivo_usuarios, 'w') as archivo:
            json.dump(list(self.usuarios_registrados), archivo, indent=4)

    def cargar_prestamos(self):
        try:
            with open(self.archivo_prestamos, 'r') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return {}

    def guardar_prestamos(self):
        with open(self.archivo_prestamos, 'w') as archivo:
            json.dump(self.libros_prestados, archivo, indent=4)

    def registrar_usuario(self, usuario_id):
        if usuario_id not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario_id)
            self.guardar_usuarios()
            return True
        return False

    def mostrar_usuarios(self):
        print("Usuarios registrados:")
        for usuario in self.usuarios_registrados:
            print(usuario)

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        self.guardar_libros()

    def prestar_libro(self, isbn, usuario_id):
        libro = self.libros.get(isbn)
        if libro and not libro.prestado and usuario_id in self.usuarios_registrados:
            libro.prestado = True
            self.libros_prestados[isbn] = usuario_id
            self.guardar_libros()
            self.guardar_prestamos()
            print(f"Libro {isbn} prestado con éxito a {usuario_id}.")
        else:
            print("Libro no disponible para préstamo o usuario no registrado.")

    def devolver_libro(self, isbn):
        libro = self.libros.get(isbn)
        if libro and libro.prestado:
            libro.prestado = False
            del self.libros_prestados[isbn]
            self.guardar_libros()
            self.guardar_prestamos()
            print(f"Libro {isbn} devuelto con éxito.")
        else:
            print("Error en la devolución del libro.")

    def mostrar_libros(self):
        for libro in self.libros.values():
            estado = "Prestado" if libro.prestado else "Disponible"
            print(f"{libro.isbn}: {libro.titulo} por {libro.autor} - {estado}")

def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n1. Añadir Libro\n2. Mostrar Libros\n3. Prestar Libro\n4. Devolver Libro\n5. Registrar Usuario\n6. Mostrar Usuarios\n7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            libro = Libro(isbn, titulo, autor, categoria)
            biblioteca.añadir_libro(libro)
        elif opcion == '2':
            biblioteca.mostrar_libros()
        elif opcion == '3':
            isbn = input("ISBN del libro a prestar: ")
            usuario_id = input("ID de usuario: ")
            biblioteca.prestar_libro(isbn, usuario_id)
        elif opcion == '4':
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(isbn)
        elif opcion == '5':
            usuario_id = input("ID de usuario a registrar: ")
            if biblioteca.registrar_usuario(usuario_id):
                print(f"Usuario {usuario_id} registrado con éxito.")
            else:
                print(f"El usuario {usuario_id} ya está registrado.")
        elif opcion == '6':
            biblioteca.mostrar_usuarios()
        elif opcion == '7':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()