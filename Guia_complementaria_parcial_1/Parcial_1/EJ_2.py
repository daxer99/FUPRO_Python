'''Escriba un programa en Python donde genere un conjunto de 500 datos aleatorios entre -50 y 50. Luego, informe la cantidad de cambios de signo entre los datos.'''

import random as r

datos = [r.randint(-50,50) for i in range(25)]
c = 0
for i in range(1,len(datos)):
    if datos[i-1]*datos[i] < 0:
        c = c + 1
print(datos)
print("Cambios de signo: ",c)