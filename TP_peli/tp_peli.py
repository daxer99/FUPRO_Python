
#1
data = []
filename = "tmdb_movies_data.csv"
with open(filename) as file:
    header = file.readline()
    for f in file:
        fila = f.split(sep=",")
        data.append([fila[0],fila[1].split(sep="|"),fila[2].split(sep="|"),int(fila[3]),fila[4].split(sep="|"),
                    fila[5].split(sep="|"),int(fila[6]),float(fila[7]),float(fila[8])])

# #2
# #A
# data_recaudacion = []
# for fila in data:
#     if fila[7] > 0 and fila[8] > 0:
#         recaudacion = fila[8]-fila[7]
#         data_recaudacion.append([fila[0],fila[6],recaudacion])
#
# with open("peliculas_recaudacion.csv","w") as file:
#     file.write("Pelicula,Año de estreno,Ganancia\n")
#     for i in range(len(data_recaudacion)):
#         file.write(data_recaudacion[i][0]+","+str(data_recaudacion[i][1])+","+str(data_recaudacion[i][2])+"\n")
#
# #B
# exito = sorted(data_recaudacion,key = lambda x:x[2],reverse=True)
# fracaso = sorted(data_recaudacion,key = lambda x:x[2],reverse=False)
# with open("Top10_exitos_y_fracasos.txt","w") as file:
#     file.write("TOP 10 Exitos,,\n")
#     file.write("Pelicula,Año de estreno,Ganancia\n")
#     for i in range(10):
#         file.write(exito[i][0] + "," + str(exito[i][1]) + "," + str(exito[i][2]) + "\n")
#     file.write("TOP 10 Fracasos,,\n")
#     file.write("Pelicula,Año de estreno,Ganancia\n")
#     for i in range(10):
#         file.write(fracaso[i][0] + "," + str(fracaso[i][1]) + "," + str(fracaso[i][2]) + "\n")