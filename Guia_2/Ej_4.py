"""
Deseamos saber si un estudiante de colegio secundario vota en las próximas elecciones legislativas a llevarse a cabo el próximo 24 de octubre, para ello debe ser mayor de 16  años.
Escriba un programa en Python donde se ingrese la fecha de nacimiento del estudiante con formato día, mes, año y se informe si vota o no.
"""

print('Ingrese fecha de nacimiento: ')
dia = int(input())
mes = int(input())
anio = int(input())

dia_eleccion = 24
mes_eleccion = 10
anio_eleccion = 2021

if (anio_eleccion - anio) >= 16:
    print('Vota')
elif (anio_eleccion - anio) == 15:
    if mes < mes_eleccion:
        print('Vota')
    elif dia <= dia_eleccion:
        print('Vota')
    else:
        print('No vota')
else:
    print('No vota')