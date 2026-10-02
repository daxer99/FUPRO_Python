'''13. Se analiza el crecimiento de 6 poblaciones bacterianas durante 15 días.
Para cada población se ingresa:
número de población
cantidad de bacterias por día
Se pide:
a) Calcular el crecimiento total (día 15 - día 1) por población.
b) Determinar cuántas poblaciones duplicaron su tamaño.
c) Informar la población con mayor tamaño final.
d) Calcular el promedio de crecimiento diario de cada población.'''

poblacion_x2 = 0
mayor_dia_15 = 0
mayor_poblacion = 0
for i in range(6):
    poblacion = int(input('Ingrese numero de poblacion: '))
    suma = 0
    for j in range(15):
        dia = str(j+1)
        bacterias = int(input('Ingrese cantidad de bacterias dia '+dia+':'))
        suma +=bacterias
        if j == 0:
            dia_1 = bacterias
        if j==14:
            dia_15 = bacterias
        print('promedio de crecimiento diario, dia',j+1,':',suma/(j+1))
    
    crecimiento = dia_15-dia_1
    print(crecimiento)
    
    if dia_1*2 >= dia_15:
        poblacion_x2+=1 
    
    if dia_15>mayor_dia_15:
        mayor_dia_15 = dia_15
        mayor_poblacion = i+1 
        
