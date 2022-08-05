"""
Escriba un programa en Python que reciba por parte del usuario la fecha como un número entero en formato aaaammdd
y que muestre por pantalla: “La fecha es: dd del mm de aaaa”
"""

fecha = int(input('Ingrese fecha: '))

anio = int(fecha / 10000)
mes = int((fecha % 10000) / 100)
dia = int(fecha % 100)

print('La fecha es: ',dia, 'del', mes ,'de', anio)