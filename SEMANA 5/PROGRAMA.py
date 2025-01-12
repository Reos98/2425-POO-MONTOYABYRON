"""
Este programa calcula el área de diferentes figuras geométricas.
El usuario puede elegir entre calcular el área de un círculo, un triángulo o un rectángulo.
"""

import math

def calcular_area_circulo(radio):
  """Calcula el área de un círculo dado su radio.

  Args:
    radio: El radio del círculo.

  Returns:
    El área del círculo.
  """
  area = math.pi * radio**2
  return area

def calcular_area_triangulo(base, altura):
  """Calcula el área de un triángulo dadas su base y altura.

  Args:
    base: La longitud de la base del triángulo.
    altura: La altura del triángulo.

  Returns:
    El área del triángulo.
  """
  area = (base * altura) / 2
  return area

def calcular_area_rectangulo(base, altura):
  """Calcula el área de un rectángulo dadas su base y altura.

  Args:
    base: La longitud de la base del rectángulo.
    altura: La altura del rectángulo.

  Returns:
    El área del rectángulo.
  """
  area = base * altura
  return area

# Obtener la figura que el usuario desea calcular
figura = input("Ingrese la figura (circulo, triangulo, rectangulo): ")

# Calcular el área según la figura seleccionada
if figura == "circulo":
  radio = float(input("Ingrese el radio del círculo: "))
  area = calcular_area_circulo(radio)
elif figura == "triangulo":
  base = float(input("Ingrese la base del triángulo: "))
  altura = float(input("Ingrese la altura del triángulo: "))
  area = calcular_area_triangulo(base, altura)
elif figura == "rectangulo":
  base = float(input("Ingrese la base del rectángulo: "))
  altura = float(input("Ingrese la altura del rectángulo: "))
  area = calcular_area_rectangulo(base, altura)
else:
  print("Figura no válida.")

# Mostrar el resultado
if "area" in locals():
  print("El área es:", area)