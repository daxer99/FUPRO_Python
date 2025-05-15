'''4. Se ingresan por pantalla los informes diarios de casos reportados de infectados por COVID19
durante los meses de marzo a noviembre inclusive en los 16 departamentos de una provincia.
Se ingresan los datos de la siguiente manera: depto, mes, cantidad de casos reportados.
Escriba un programa que organice una matriz de 16 filas (departamentos) por 9 columnas (meses) y obtenga e informe:
a) El % de casos registrados en el depto 5 del mes de mayo, respecto de todos los casos que se registraron en ese mes en la provincia.
b) La menor cantidad de casos registrada en julio y en qué depto ocurrió.
c) Qué % de aumento de casos se dio en el depto 11 en junio respecto de mayo?'''
from Guia_3.Ej_3 import menor

#mar-abr-may-jun-jul-ago-sep-oct-nov
# 0   1   2   3   4   5   6   7   8

datos = [[0]*9 for i in range(16)]

depto = int(input('Ingrese depto, 0 para terminar: '))
while depto != 0:
    mes = int(input('Ingrese mes: '))
    casos = int(input('Ingrese cantidad de casos: '))
    datos[depto-1][mes-1]+=casos

    depto = int(input('Ingrese depto, 0 para terminar: '))

#A
total_casos_mayo = 0
for i in range(len(datos)):
    total_casos_mayo += datos[i][2]
print(round(datos[4][2]/total_casos_mayo*100,2),'% es el porcentaje de casos registrados en el depto 5 del mes de mayo, respecto de todos los casos que se registraron en ese mes en la provincia')

#B
menor_julio = 0
depto_menor_julio = 0
for i in range(len(datos)):
    if datos[i][4] > menor_julio:
        menor_julio = datos[i][4]
        depto_menor_julio = i+1
print('La menor cantidad de casos registrada en julio fue de',menor_julio,' en el depto',depto_menor_julio)

#C
print('El % de diferencia entre junio y mayo para los casos del depto 11 es de:',abs(datos[10][3]-datos[10][2])/datos[10][3]*100,'%')