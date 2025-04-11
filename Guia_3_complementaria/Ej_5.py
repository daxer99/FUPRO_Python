'''5. Un grupo de investigadores analiza el comportamiento de 17 ratones de laboratorio a quienes se le suministró una hormona de crecimiento y se les midió el peso durante 56 días a cada uno.
Para ello se ingresan ordenadamente: el nº de ratón y luego los 56 valores de peso obtenidos en el período; luego el siguiente nº de ratón y sus 56 valores de peso; así sucesivamente.
Escriba un programa que calcule e informe:
a) los gramos de peso ganados en cada semana para cada ratón.
b) ¿Cuántos ratones superaron el peso de 580 gr al final de período?
c) El nº del ratón que logró el mayor peso.'''

import random
ratones_mas_580 = 0
raton_mayor_peso = 0
mayor_peso = 0

for i in range(17):
    for j in range(8):
        for k in range(7):
            peso = random.randint(540,620)
            if k == 0:
                peso_inicial = peso
            if k == 6:
                peso_final = peso
        print("Los gramos ganados por el raton",i+1,'en la semana',j+1,'fueron',abs(peso_final-peso_inicial))

    peso_definitivo = peso

    if peso_definitivo > 580:
        ratones_mas_580+=1

    if peso_definitivo > mayor_peso:
        mayor_peso = peso_definitivo
        raton_mayor_peso = i+1



print(ratones_mas_580,"superaron los 580gr")
print("El raton de mayor peso fue el numero",raton_mayor_peso)
