"""
Se solicita un programa en Python que calcule las soluciones o raíces de una ecuación cuadrática del tipo ax2+bx+c=0, siendo que el usuario del programa ingresa como datos los coeficientes a, b y c. Suponga que el usuario siempre ingresa datos que corresponden a ecuaciones de raíces reales.
"""
from math import sqrt

A = float(input("Ingrese el coeficiente de la variable cuadrática\n"))
B = float(input("Ingrese el coeficiente de la variable lineal\n"))
C = float(input("Ingrese el término independiente\n"))

x1 = (-B + sqrt(B ** 2 - (4 * A * C))) / (2 * A)
x2 = (-B - sqrt(B ** 2 - (4 * A * C))) / (2 * A)

print("Las soluciones de la ecuación son:")
print('X1 = ', x1)
print('X2 = ', x2)