# Clase que representa un gestor de archivos
class FileManager:
    # Constructor: se utiliza para inicializar los atributos del objeto
    def __init__(self, file_name, mode):
        """
        Este es el constructor de la clase FileManager.
        Inicializa el nombre del archivo y abre el archivo en el modo indicado.
        """
        self.file_name = file_name  # Nombre del archivo
        self.mode = mode  # Modo de apertura del archivo (lectura/escritura)
        try:
            # Se intenta abrir el archivo
            self.file = open(file_name, mode)
            print(f"Archivo '{file_name}' abierto en modo '{mode}'.")
        except Exception as e:
            print(f"Error al intentar abrir el archivo '{file_name}': {e}")
            self.file = None  # Si ocurre un error, se asigna None al archivo

    # Método para escribir en el archivo
    def write_to_file(self, text):
        """
        Este método escribe texto en el archivo si está abierto en modo escritura.
        """
        if self.file and self.mode in ('w', 'a'):
            try:
                self.file.write(text)
                print(f"Texto escrito en el archivo '{self.file_name}'.")
            except Exception as e:
                print(f"Error al intentar escribir en el archivo '{self.file_name}': {e}")
        else:
            print(f"No se puede escribir en el archivo '{self.file_name}'. Verifica el modo de apertura.")

    # Método para leer el archivo
    def read_file(self):
        """
        Este método lee y devuelve el contenido del archivo si está abierto en modo lectura.
        """
        if self.file and self.mode == 'r':
            try:
                content = self.file.read()
                print(f"Contenido leído del archivo '{self.file_name}':")
                print(content)
                return content
            except Exception as e:
                print(f"Error al intentar leer el archivo '{self.file_name}': {e}")
                return None
        else:
            print(f"No se puede leer del archivo '{self.file_name}'. Verifica el modo de apertura.")
            return None

    # Destructor: se utiliza para liberar recursos cuando el objeto ya no se necesita
    def __del__(self):
        """
        Este es el destructor de la clase FileManager.
        Cierra el archivo si está abierto y realiza una limpieza de recursos.
        """
        if self.file:
            try:
                self.file.close()  # Cierra el archivo
                print(f"Archivo '{self.file_name}' cerrado.")
            except Exception as e:
                print(f"Error al intentar cerrar el archivo '{self.file_name}': {e}")
        else:
            print(f"No hay archivo que cerrar para '{self.file_name}'.")


# DEMOSTRACIÓN DEL USO DE CONSTRUCTORES Y DESTRUCTORES
print("---- DEMOSTRACIÓN DE CONSTRUCTORES Y DESTRUCTORES ----")

# Creación de un objeto FileManager en modo escritura
file_manager = FileManager("example.txt", "w")  # Constructor se activa
file_manager.write_to_file("¡Hola! Este es un ejemplo de escritura en un archivo.\n")

# Eliminamos el objeto explícitamente para demostrar el destructor
del file_manager  # Destructor se activa automáticamente

# Creación de un objeto FileManager en modo lectura
file_manager2 = FileManager("example.txt", "r")  # Constructor se activa
file_manager2.read_file()

# Eliminamos el objeto explícitamente
del file_manager2  # Destructor se activa automáticamente

print("---- FIN DEL PROGRAMA ----")
