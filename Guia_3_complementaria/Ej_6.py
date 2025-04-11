'''6-Una empresa distribuidora comercializa 25 artículos.
Posee 4 sucursales y desea analizar el desempeño de las mismas.
Para ello se ingresan los datos correspondientes a las ventas efectuadas en el último año:
código sucursal (1…4), código artículo (1…25), cantidad unidades vendidas. Determine e informe:
a. El total de unidades vendidas por la sucursal 3, sumando todos los artículos.
b. La cantidad vendida por la sucursal 1 del artículo 6. '''

import random as r
sucursal_3 = 0
sucursal_1_articulo_3 = 0
for i in range(4):
    for j in range(25):
        monto = r.uniform(50,120)
        if i == 0 and j == 2:
            sucursal_1_articulo_3 = monto
    if i == 2:
        sucursal_3 += monto

print('Total de ventas sucursal 3:',sucursal_3)
print('Total de ventas del articulo 3 de la sucursal 1:',sucursal_1_articulo_3)