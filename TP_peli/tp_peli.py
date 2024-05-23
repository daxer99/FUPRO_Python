from funciones import filtrarXdirector,filtrarXanio,filtrarXcompania,filtrarXactor,filtrarXgenero

def convertir_minutos(minutos_totales):
    horas = minutos_totales // 60
    minutos = minutos_totales % 60
    return horas, minutos

def lista_unica(lista):
    lista_unica = []
    for elemento in lista:
        if elemento not in lista_unica:
            lista_unica.append(elemento)
    return lista_unica

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

#Llamado 1
#4
# lista_anios = []
# for fila in data:
#     lista_anios.append(fila[6])
# lista_unica_anios = lista_unica(lista_anios)
#
# mayor_cant_peliculas = 0
# anio_mayor_cant_peliculas = 0
# for i in range(len(lista_unica_anios)):
#     cant_peliculas = len(filtrarXanio(data,lista_unica_anios[i]))
#     if cant_peliculas > mayor_cant_peliculas:
#         mayor_cant_peliculas = cant_peliculas
#         anio_mayor_cant_peliculas = lista_unica_anios[i]
#
# print(anio_mayor_cant_peliculas)
# print(mayor_cant_peliculas)

#5
# lista_companias = []
# for fila in data:
#     for i in fila[5]:
#         lista_companias.append(i)
# cant_companias = len(lista_unica(lista_companias))
# print(cant_companias)

#6
# cont = 0
# for fila in data:
#     if "Leonardo DiCaprio" in fila[1] and "Martin Scorsese" in fila[2]:
#         cont +=1
# print(cont)

#7
# cont = 0
# for fila in data:
#     if "Chris Evans" in fila[1] and "Marvel Studios" in fila[5]:
#         cont +=1
# print(cont)

#8
# cont = 0
# for fila in data:
#     if "Action" in fila[4] and "Fantasy" in fila[4]:
#         cont +=1
# print(cont)

#9
# cont = 0
# for fila in data:
#     if fila[3]/60 > 3:
#         cont +=1
# print(cont)

#10
# minutos_totales = 0
# for fila in data:
#     if fila[0].find("Indiana Jones") !=-1:
#         minutos_totales += fila[3]
#
# hh,mm = convertir_minutos(minutos_totales)
# print(hh,":",mm)
