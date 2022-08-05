"5. Escribir un programa en Python que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desvío."

import math

valores = input('Ingrese valores separados por coma:\n')
lista = valores.split(',')
#convert string list in a float list
for i in range(len(lista)):
    lista[i] = float(lista[i])

#obtener media
suma = 0
for i in range(len(lista)):
    suma = suma + lista[i]
media = suma / len(lista)
media = round(media,2)

#obtener desvio
suma_cuadrados = 0
cuadrados = []
for i in range(len(lista)):
    cuadrados.append(pow(lista[i]-media,2))
for i in range(len(lista)):
    suma_cuadrados = suma_cuadrados + cuadrados[i]
desvio = math.sqrt(suma_cuadrados/len(lista))
desvio = round(desvio,2)

print('La media es', media, 'y el desvio es', desvio)

