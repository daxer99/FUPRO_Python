"""
Escriba un programa que pida al usuario su peso (en kg) y estatura (en metros),
calcule el índice de masa corporal y lo almacene en una variable,
y muestre por pantalla la frase
Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
"""

peso = float(input('Ingrese su peso en Kgs: '))
altura = float(input('Ingrese su altura en mts: '))

indice_masa_corporal = peso/(altura*altura)
indice_masa_corporal = round(indice_masa_corporal,2)

print('Su indice de masa corporal es:', indice_masa_corporal)