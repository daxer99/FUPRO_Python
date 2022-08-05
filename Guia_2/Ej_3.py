'''Diseñe e implemente un programa en Python que calcule el Índice de masa corporal (IMC) de una persona a partir del peso
 y altura ingresados por un usuario.
 Informar la condición del usuario a partir de los valores obtenidos de IMC según la siguiente tabla:'''

peso = float(input('Ingrese su peso en Kgs: '))
altura = float(input('Ingrese su altura en mts: '))

indice_masa_corporal = peso/(altura*altura)
indice_masa_corporal = round(indice_masa_corporal,2)

if indice_masa_corporal <= 18.5:
    print('Estado de infrapeso')
elif 1.85 < indice_masa_corporal <= 25:
    print('Estado normal')
elif 25 < indice_masa_corporal <= 30:
    print('Estado de sobrepeso')
else:
    print('Estado de obesidad')