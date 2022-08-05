'''8. Una Empresa paga a sus 100 operarios semanalmente de acuerdo con la cantidad de horas trabajadas,
a razón de X pesos la hora hasta 40 hs. y un 50% más por todas las horas que pasan de 40.
Informar el total de salario a cobrar por cada trabajador.'''

import random as rd

cantidad_empleados = 10
precio_hora = 576
for i in range(cantidad_empleados):
    horas_trabajadas = rd.randint(30,50)
    if horas_trabajadas <= 40:
        salario = horas_trabajadas*precio_hora
        print("El trabajador ",i+1," cobra: $", salario)
    else:
        salario = horas_trabajadas*precio_hora + (horas_trabajadas-40)*precio_hora*1.50
        print("El trabajador ", i + 1, " cobra: $", salario)
