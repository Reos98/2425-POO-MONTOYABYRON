class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print("Libro prestado")
        else:
            print("Libro no disponible")

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.disponible:
            libro.prestar()
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha prestado {libro.titulo}")
        else:
            print("El libro no está disponible")

# Ejemplo de uso
libro1 = Libro("Don Quijote", "Miguel de Cervantes", "12345")
usuario1 = Usuario("Juan Pérez", 123)
usuario1.prestar_libro(libro1)