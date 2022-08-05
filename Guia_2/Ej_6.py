'''Escriba un programa que pida el radio, las coordenadas del centro de una circunferencia y las coordenadas de un punto y que indique si el punto está sobre la circunferencia, dentro o fuera de ella.
Se recuerda que un punto está fuera, dentro o sobre la circunferencia según sea la relación entre el radio y la distancia entre el punto y el centro de la circunferencia.'''

import math

print('Ingrese centro (x,y): \n')
centro_x = float(input('X: '))
centro_y = float(input('Y: '))

radio = float(input('Ingrese radio: '))
radio = round(radio,2)

print('Ingrese punto (x,y): \n')
punto_x = float(input('X: '))
punto_y = float(input('Y: '))

distancia_centro_punto = math.sqrt(pow((punto_x-centro_x),2) + pow((punto_y-centro_y),2))
distancia_centro_punto = round(distancia_centro_punto,2)


if radio == distancia_centro_punto:
    print('El punto se encuentra sobre la circunferencia')
elif radio > distancia_centro_punto:
    print('El punto se encuentra dentro de la circunferencia')
else:
    print('El punto se encuentra fuera de la circunferencia')