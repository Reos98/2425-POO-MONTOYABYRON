import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'SEMANA 2/EJEMPLO DE TECNICAS DE PROGRAMACION.py',
        '2': 'SEMANA 3/POO.py',
        '3': 'SEMANA 3/TRADICIONAL.py',
        '4': 'SEMANA 4/EjemplosMundoReal_POO/SIMULADOR DE UNA TIENDA EN LINEA.py',
        '5': 'SEMANA 4/EjemplosMundoReal_POO/SISTEMA DE GESTION DE UNA BIBLIOTECA.py',
        '6': 'SEMANA 5/PROGRAMA.py',
        '7': 'SEMANA 6/TAREA SEMANA 6.py',
        '8': 'SEMANA 7/SEMANA 7.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()