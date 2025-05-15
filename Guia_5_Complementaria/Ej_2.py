import random
'''2. Escriba un programa que lea por consola el stock de cada uno de los 10 productos que comercializa una empresa. 
Posteriormente, lea los 16 pares de datos correspondientes a ventas realizadas en la empresa en un día; se leen: código y cantidad. 
Cada vez que lea un par de datos nuevos se debe actualizar el stock y si este no es suficiente para realizar la venta se debe informar al usuario el stock disponible de ese producto. 
Una vez finalizada la carga de datos se debe informar al usuario el stock final de cada producto.'''

L = []
for i in range(10):
    L.append(random.randint(53,268))

for i in range (16):
    cod_art = random.randint(0,9)
    ventas = random.randint(1,50)
    if ventas > L[cod_art]:
        print('No hay stock suficiente del articulo. Disponible:',L[i])
    else:
        L[cod_art]-=ventas