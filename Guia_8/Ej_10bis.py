filename = "cantidad-consultas-medicas-ambulatorias.csv"
datos = []
with open(filename) as file:
    header = file.readline()
    for f in file:
        fila = f.split(sep=",")
        datos.append([fila[0],fila[1],int(fila[2]),int(fila[3]),int(fila[4]),int(fila[5]),int(fila[6]),int(fila[7])])

header = header.strip("\n").split(sep = ",")

sum_columns = []
for j in range(2,len(datos[0])):
    sum = 0
    for i in range(len(datos)):
        sum += datos[i][j]
    sum_columns.append(sum)
print(sum_columns)

mayores_consultas_anio = []
mayor = 0
unidad_op =""
for j in range(2,len(datos[0])):
    for i in range(len(datos)):
        if mayor < datos[i][j]:
            mayor = datos[i][j]
            unidad_op = datos[i][1]
    mayores_consultas_anio.append([unidad_op,mayor])
print(mayores_consultas_anio)