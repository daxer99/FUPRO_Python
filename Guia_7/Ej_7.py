'''Se ingresan el año (int) y luego 12 temperaturas máximas (float) de cada mes registradas en un año en una localidad.
Los 10 años analizados van entre 1990 y 1999. Organice la información en una estructura de datos,  determine e informe:
a) El año de mayor temperatura máxima en febrero. Crear una función.
b) Qué % disminuyó la temperatura máxima  entre el valor de Enero y el de Julio de 1995. Crear una función.
c) El promedio de las seis temperaturas máximas en todo el año 1991.'''

import random as r

def anio_max_temp_feb(tabla):
    max_temp = 0
    anio_max_temp = 0
    for i in range(len(tabla)):
        if tabla[i][1] > max_temp:
            max_temp = tabla[i][1]
            anio_max_temp = i
    return 1990 + anio_max_temp

def disminucion_pocentual_enero_julio_1995(lista):
    return round((lista[0]-lista[6])/lista[0] * 100,2)

def prom_6_temp_max_1991(lista):
    lista_ord = sorted(lista,reverse=True)
    prom = sum(lista_ord[0:5])/6
    return round(prom,2)

#defino el contenedor de los datos
rows, cols = 10,12
matrix = [([0]*cols) for i in range(rows)]

#Lleno el contenedor de los datos
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        #matrix[i][j] = float(input("ingrese temperatura maxima: "))
        matrix[i][j] = r.randint(28,45)

#A
print("El año de mayor temperatura máxima en febrero fue",anio_max_temp_feb(matrix))
#B
print("El % que disminuyó la temperatura máxima  entre el valor de Enero y el de Julio de 1995 fue del",disminucion_pocentual_enero_julio_1995(matrix[5]),"%")
#C
print("El promedio de las seis temperaturas máximas en todo el año 1991 fue de",prom_6_temp_max_1991(matrix[1]),"ºC")