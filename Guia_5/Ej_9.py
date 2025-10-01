'''Escriba un programa que genere al azar 1000 coordenadas en el plano con valores de "x"
comprendidos entre -50 y 100, y valores de "y" comprendidos entre -10 y 25. Posteriormente
el programa debe solicitar las coordenadas del centro y el valor del radio de una circunferencia
e indicar cuántos de los puntos del plano se encuentran dentro de la circunferencia.'''

import random as rd
import math as m

x = []
y = []
for i in range(0, 1000):
    x.append(rd.randint(-50, 100))
    y.append(rd.randint(-10, 25))

cx = int(input("Ingrese coordenada X: "))
cy = int(input("Ingrese coordenada Y: "))
radio = int(input("Ingrese radio: "))

cont = 0

for i in range(0, 1000):
    dist = m.sqrt(pow(cx - x[i], 2) + pow(cy - y[i], 2))
    if radio <= dist:
        cont = cont + 1

print(cont, " puntos se encuentran dentro de la circunferencia")