class Semana:
    """Representa una semana y permite calcular el promedio de temperatura."""

    def __init__(self):
        self.temperaturas = []

    def ingresar_datos(self):
        """Ingresa las temperaturas diarias."""
        for dia in range(1, 8):
            temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.temperaturas.append(temperatura)

    def calcular_promedio(self):
        """Calcula el promedio de las temperaturas."""
        suma = sum(self.temperaturas)
        promedio = suma / len(self.temperaturas)
        return promedio

# Creamos un objeto de la clase Semana
semana = Semana()

# Ingresamos los datos
semana.ingresar_datos()

# Calculamos y mostramos el promedio
promedio_semanal = semana.calcular_promedio()
print(f"El promedio semanal de temperatura es: {promedio_semanal:.2f} °C")