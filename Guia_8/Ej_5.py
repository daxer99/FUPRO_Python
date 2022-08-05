rows, cols = 10,12
matrix = [([0]*cols) for i in range(rows)]

def date_to_month(date):
    return int(date[2:4])

def max_export_march(matrix):
    mayor = matrix[0][2]
    indice_mayor = 0
    for i in range(len(matrix)):
        if matrix[i][2] > mayor:
            mayor = matrix[i][2]
            indice_mayor = i
    return indice_mayor

export = []
with open("export.txt") as file:
    for fila in file:
        export.append(fila.strip('\t\n').split(sep = " "))

for i in range(len(export)):
    #print(export[i][0]," ",export[i][1]," ",export[i][2])
    matrix[int(export[i][0])-1][date_to_month(export[i][1])-1] += int(export[i][2])

for i in range(rows):
    print("Total exportado al pais ",i+1," : ",sum(matrix[i]))

print("")
print("Pais con mayor monto exportado en marzo de 2021: ",max_export_march(matrix)+1)