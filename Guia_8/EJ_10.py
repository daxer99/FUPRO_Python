def sumColumn(matrix, columnIndex):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][columnIndex]
    return sum


def maxConsultasAnio(matrix, columnIndex):
    mayor = 0
    unidad_op = ""
    for i in range(len(matrix)):
        if mayor < matrix[i][columnIndex]:
            mayor = matrix[i][columnIndex]
            unidad_op = matrix[i][1]
    return [unidad_op, mayor]


def menos1000consultas(matrix, columnIndex):
    unidades = []
    unidad_op = ""
    for i in range(len(matrix)):
        if 1000 > matrix[i][columnIndex]:
            unidad_op = matrix[i][1]
            unidades.append(unidad_op)
    return unidades


filename = "cantidad-consultas-medicas-ambulatorias.csv"
datos = []
with open(filename) as file:
    header = file.readline()
    for f in file:
        fila = f.split(sep=",")
        datos.append(
            [fila[0], fila[1], int(fila[2]), int(fila[3]), int(fila[4]), int(fila[5]), int(fila[6]), int(fila[7])])

header = header.strip("\n").split(sep=",")

print("Total de consultas por año: \n")
total_consultas_anio = []
for i in range(2, len(datos[0])):
    total_consultas_anio.append(sumColumn(datos, i))
for i in range(len(total_consultas_anio)):
    print(header[i + 2], ": ", total_consultas_anio[i])
    print("")

print("Unidad con mayor cantidad de consultas por año: \n")
mayores_consultas_anio = []
for i in range(2, len(datos[0])):
    mayores_consultas_anio.append(maxConsultasAnio(datos, i))
for i in range(len(mayores_consultas_anio)):
    print(header[i + 2], ": ", mayores_consultas_anio[i])
    print("")

print("Unidades con menos de 1000 consultas por año: \n")
menos_1000_consultas_anio = []
for i in range(2, len(datos[0])):
    menos_1000_consultas_anio.append(menos1000consultas(datos, i))
for i in range(len(menos_1000_consultas_anio)):
    print(header[i + 2], ": ", menos_1000_consultas_anio[i])
    print("")

consultas_totales_por_unidad = []
for i in range(len(datos)):
    consultas_totales_por_unidad.append(sum(datos[i][2:len(datos[0])]))

unidad_totales = list(zip([row[1] for row in datos], consultas_totales_por_unidad))
unidad_totales_sorted = sorted(unidad_totales, key=lambda x: x[1], reverse=True)

with open("Top10Consultas.txt", "w") as file:
    file.write("Unidad Operativa,Total Historico de consultas (2013-2018)\n")
    for i in range(0, 10):
        file.write(unidad_totales_sorted[i][0] + "," + str(unidad_totales_sorted[i][1]) + "\n")