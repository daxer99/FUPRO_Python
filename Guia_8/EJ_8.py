from operator import itemgetter
import csv

paises = []
casos_activos = []

# with open("covid.csv") as file:
#     header = file.readline()
#     for f in file:
#         fila = f.split(sep=",")
#         paises.append(fila[0])
#         casos_activos.append(int(fila[4].strip("\n")))

# Leer datos con CSV
with open('covid.csv') as csv_file:
    archivo = csv.reader(csv_file, delimiter=',')
    header = next(archivo)
    for fila in archivo:
        paises.append(fila[0])
        casos_activos.append(int(fila[4].strip("\n")))

datos = list(zip(paises, casos_activos))

# datos_ordenados = sorted(datos, key = lambda x:x[1],reverse = True)
datos_ordenados = sorted(datos, key=itemgetter(1), reverse=True)

with open("Ranking5Covid.txt", "w") as file:
    file.write("Pais,Casos Activos")
    file.write("\n")
    for i in range(5):
        file.write(datos_ordenados[i][0] + "," + str(datos_ordenados[i][1]))
        file.write("\n")