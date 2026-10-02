'''6. Una empresa distribuidora comercializa 25 artículos. Posee 4 sucursales y desea analizar el desempeño de las mismas. 
Para ello se ingresan los datos correspondientes a las ventas efectuadas en el último año: código sucursal (1…4), código artículo (1…25), cantidad unidades vendidas. 
Determine e informe:
a. El total de unidades vendidas por la sucursal 3, sumando todos los artículos. 
b. La cantidad vendida por la sucursal 1 del artículo 6. c. El porcentaje de ventas totales efectuadas por la sucursal 3. 
d. El porcentaje de ventas totales realizadas del articulo 17.''' 

suc_3 = 0
suc_1_art_6 =0
total_ventas = 0
art_17 = 0    

suc = int(input('Ingrese sucursal, 0 para terminar: '))
while suc !=0:
    art = int(input('Ingrese articulo: '))
    cantidad = int(input('Ingrese cantidad: '))
    
    total_ventas += cantidad
    
    if suc == 3:
        suc_3+=1 
    if suc == 1 and art == 6:
        suc_1_art_6 +=1 
    if art == 17:
        art_17 += 1 

print(suc_3)
print(suc_1_art_6)
print(suc_3/total_ventas*100)
print(art_17/total_ventas*100)
