"""
Diseñe e implemente un programa en Python que calcule el área y el perímetro de un círculo cuyo radio se ingresa como dato.
"""

radio = input('Ingrese radio: ')
radio = float(radio)
pi = 3.14
area = pi * radio * radio
area = round(area,2)
perimetro = 2 * pi * radio
perimetro = round(perimetro,2)
print('El area es:', area)
print('El perimetro es:', perimetro)