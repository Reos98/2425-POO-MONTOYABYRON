def ingresar_datos_diarios():
    """Ingresa las temperaturas diarias de una semana y las almacena en una lista."""
    temperaturas = []
    for dia in range(1, 8):
        temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio(temperaturas):
    """Calcula el promedio de una lista de temperaturas."""
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

# Llamamos a las funciones
temperaturas_semanales = ingresar_datos_diarios()
promedio_semanal = calcular_promedio(temperaturas_semanales)
print(f"El promedio semanal de temperatura es: {promedio_semanal:.2f} °C")