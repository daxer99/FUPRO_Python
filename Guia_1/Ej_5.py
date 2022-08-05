"""
Ejercicio5:
Diseñe e implemente un programa en Python que permita ingresar un valor numérico correspondiente a una medida en pies y devuelva la cantidad equivalente en metros. Nota: 1 pie = 0,3048 metros.
"""

valor_metros = input('Ingrese valor en metros: ') #Se asigna el valor de consola en valor_metros
valor_metros = int(valor_metros)  #Se castea el valor de consola de string a int
valor_pies = valor_metros / 0.3048 #Se convierte de metros a pies
valor_pies = round(valor_pies,2)   #Se redondea el flotante a 2 decimales

print(valor_metros, 'metros son', valor_pies, 'pies') #Se muestra el resultado por pantalla