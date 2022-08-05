''' Una película ha costado 150 millones de dólares. La primera semana, la película tiene un costo de 31 millones de dólares. Cada semana que pasa, la factura es el 20% inferior a la de la semana anterior.
Escriba un programa que indique el número de semanas que se puede permitir la película para su producción.'''

costo_total = 150000000
costo_semana_1 = 30000000
semanas_produccion = 1
costo_actual = costo_semana_1

while costo_actual < costo_total:
    costo_actual = costo_actual + costo_actual * 0.2
    semanas_produccion = semanas_produccion +1
    print('Costo semana', semanas_produccion,':', costo_actual)

print('La película se puede permitir unas',semanas_produccion, 'semanas de producción')