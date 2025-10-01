'''Una empresa distribuidora comercializa 25 artículos. Posee 4 sucursales y desea analizar el desempeño de las mismas.
Para ello se ingresan los datos correspondientes a las ventas efectuadas en cierto período: código sucursal (1…4), código artículo (1…25), cantidad unidades vendidas.
El ingreso de datos finaliza con el código de sucursal 0.
Determine e informe:
a. Las cantidades de unidades vendidas por la empresa de cada artículo.
b. El total de unidades vendidas por la sucursal 3, sumando todos los artículos.
c. La cantidad vendida por la sucursal 1 del artículo 6.
d. La sucursal que vendió más unidades del artículo 8.'''

rows, cols = 4,25
matrix = [([0]*cols) for i in range(rows)]

sucursal = int(input("Ingrese sucursal (1-4): "))
while sucursal !=0:
    cod_articulo = int(input("Ingrese codigo de articulo: "))
    cant_vendida = int(input("Ingrese cantidad vendida: "))
    matrix[sucursal-1][cod_articulo-1]+=cant_vendida
    sucursal = int(input("Ingrese sucursal (1-4, 0 para terminar): "))

#A
column_sums = []
suma = 0
for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        suma += matrix[j][i]
    column_sums.append(suma)
    suma = 0
print(column_sums)
# column_sums_2 = [sum([row[i] for row in matrix]) for i in range(len(matrix[0]))]
# print(column_sums_2)

#B
# print("El total de unidades vendidas por la sucursal 3 fue de: ",sum(matrix[2]))
suma = 0
for i in range(len(matrix[0])):
    suma+=matrix[2][i]
print("El total de unidades vendidas por la sucursal 3 fue de: ",suma)

#C
print("La cantidad vendida por la sucursal 1 del artículo 6 fue de: ",matrix[0][5])

#D
sucursal_mas_unidades_art_8 = 0
mayor = 0
for i in range(len(matrix)):
    if mayor < matrix[i][7]:
        mayor = matrix[i][7]
        sucursal_mas_unidades_art_8 = i+1
print("La sucursal que vendió más unidades del artículo 8 fue la nro ",sucursal_mas_unidades_art_8)