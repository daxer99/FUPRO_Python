import csv
#Punto 1
def leer_csv(nombre_archivo):
    lista = []
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        interprete = csv.reader(archivo, delimiter=",")
        cabecera = next(interprete)
        for fila in interprete:
            lista.append(fila)
    return lista
netflix_data = leer_csv('netflix.csv')
netflix_data_series = []
netflix_data_peliculas = []
for fila in netflix_data:
    if fila[0] == 'Movie':
        netflix_data_peliculas.append(fila)
    elif fila[0] == 'TV Show':
        netflix_data_series.append(fila)

movies_imdb_data = leer_csv('imdb_top_1000_movies.csv')
series_imdb_data = leer_csv('imdb_top_1000_series.csv')

#Punto 2
# action_movies_netflix =[]
# for i in range(len(netflix_data)):
#     if netflix_data[i][0] == 'Movie':
#         if 'action' in netflix_data[i][9].lower():
#             action_movies_netflix.append(netflix_data[i][1])
# action_movies_netflix_imdb = []
# for i in range(len(action_movies_netflix)):
#     for j in range(len(movies_imdb_data)):
#         if action_movies_netflix[i].lower() == movies_imdb_data[j][0].lower():
#             action_movies_netflix_imdb.append([action_movies_netflix[i],movies_imdb_data[j][2]])
# action_movies_netflix_imdb_sorted = sorted(action_movies_netflix_imdb,key=lambda x:x[1],reverse=True)
#
# with open("top_10_action_movies_netflix.csv",'w') as file:
#     file.write('Titulo,Puntuacion\n')
#     for i in range(10):
#         file.write(action_movies_netflix_imdb_sorted[i][0]+','+action_movies_netflix_imdb_sorted[i][1]+'\n')

#Punto 3
# netflix_series_00s = []
# for i in range(len(netflix_data)):
#     if netflix_data[i][0] == 'TV Show':
#         if 1999<int(netflix_data[i][6])<2010:
#             netflix_series_00s.append([netflix_data[i][1],netflix_data[i][6]])
# netflix_series_00s_imdb = []
# for i in range(len(netflix_series_00s)):
#     for j in range(len(series_imdb_data)):
#         if netflix_series_00s[i][0].lower() == series_imdb_data[j][0].lower():
#             netflix_series_00s_imdb.append([netflix_series_00s[i][0],netflix_series_00s[i][1],series_imdb_data[j][2]])
# netflix_series_00s_imdb_sorted = sorted(netflix_series_00s_imdb,key=lambda x:x[2],reverse=True)
# with open("top5_2000_2009_tv_shows.csv",'w') as file:
#     file.write('Titulo,Año,Puntuacion\n')
#     for i in range(5):
#         file.write(netflix_series_00s_imdb_sorted[i][0]+','+netflix_series_00s_imdb_sorted[i][1]+','+netflix_series_00s_imdb_sorted[i][2]+'\n')

#Punto 4
def filtrarXgenero(datos,genero):
    lista = []
    for i in range(len(datos)):
        if genero.lower() in datos[i][9].lower():
                 lista.append(datos[i][1])
    return lista

def filtrarXactor(datos,actor):
    lista = []
    for i in range(len(datos)):
        if actor.lower() in datos[i][3].lower():
            lista.append(datos[i][1])
    return lista

def filtrarXdirector(datos,director):
    lista = []
    for i in range(len(datos)):
        if director.lower() in datos[i][2].lower():
            lista.append(datos[i][1])
    return lista

def filtrarXanioAñadida(datos,anio):
    lista = []
    for i in range(len(datos)):
        if anio in datos[i][5].lower():
            lista.append(datos[i][1])
    return lista

def filtrarXanioRealizada(datos,anio):
    lista = []
    for i in range(len(datos)):
        if anio == datos[i][6]:
            lista.append(datos[i][1])
    return lista

#Punto 5
# anios = []
# for i in range(len(netflix_data_peliculas)):
#     year = netflix_data_peliculas[i][5].strip(' ').split(',')
#     if year[1].strip(' ') not in anios:
#         anios.append(year[1].strip(' '))
#
# cantidad_peliculas_realizadas_x_anio = []
# for i in range(len(anios)):
#     cantidad_peliculas_realizadas_x_anio.append([anios[i],len(filtrarXanioAñadida(netflix_data_peliculas,anios[i]))])
# ordenada = sorted(cantidad_peliculas_realizadas_x_anio,key=lambda x: x[1])
# print(ordenada[0])

#Punto 6
# anios = []
# for i in range(len(netflix_data_series)):
#     if netflix_data_series[i][6] not in anios:
#         anios.append(netflix_data_series[i][6])
#
# series_drama = []
# for fila in netflix_data_series:
#     if 'drama' in fila[9].lower():
#         series_drama.append(fila)
#
# cantidad_series_drama_realizadas_x_anio = []
# for i in range(len(anios)):
#     cantidad_series_drama_realizadas_x_anio.append([anios[i],len(filtrarXanioRealizada(series_drama,anios[i]))])
# ordenada = sorted(cantidad_series_drama_realizadas_x_anio,key=lambda x: x[1],reverse=True)
# print(ordenada[0])

#Punto 7
# pelis_spielberg = filtrarXdirector(netflix_data_peliculas,'Steven Spielberg')
# pelis_ford = filtrarXactor(netflix_data_peliculas,'Harrison Ford')
# contador = 0
#
# for i in range(len(pelis_spielberg)):
#     for j in range(len(pelis_ford)):
#         if pelis_spielberg[i].lower() == pelis_ford[j].lower():
#             contador += 1
# print(contador)

#Defensa
#1 Cuantas peliculas del genero drama tienen más de 1 director
# peliculas_drama = []
# for fila in netflix_data_peliculas:
#     if 'drama' in fila[9].lower():
#         peliculas_drama.append(fila)
# contador = 0
# for fila in peliculas_drama:
#     directores = fila[2].split(',')
#     if len(directores) > 1:
#         contador += 1
# print(contador)

#2 En que año se realizaron más series del genero acción y aventura
# anios = []
# for i in range(len(netflix_data_series)):
#     if netflix_data_series[i][6] not in anios:
#         anios.append(netflix_data_series[i][6])
#
# series_aa = []
# for fila in netflix_data_series:
#     if 'Action & Adventure' in fila[9]:
#         series_aa.append(fila)
#
# cantidad_series_aa_realizadas_x_anio = []
# for i in range(len(anios)):
#     cantidad_series_aa_realizadas_x_anio.append([anios[i],len(filtrarXanioRealizada(series_aa,anios[i]))])
# ordenada = sorted(cantidad_series_aa_realizadas_x_anio,key=lambda x: x[1],reverse=True)
# print(ordenada[0])

#3 cuantas peliculas se añadieron a la plataforma el mismo año en que fueron realizadas
# contador = 0
# for fila in netflix_data_peliculas:
#     aniadida = fila[5].split(',')
#     aniadida = int(aniadida[1])
#     realizada = int(fila[6])
#     if aniadida == realizada:
#         contador += 1
# print(contador)

# 4 En cuantas peliculas dirigidas por Quentin Tarantino actua Uma Thurman
pelis_director = filtrarXdirector(netflix_data_peliculas,'Quentin Tarantino')
pelis_actor = filtrarXactor(netflix_data_peliculas,'Uma Thurman')
contador = 0

for i in range(len(pelis_director)):
    for j in range(len(pelis_actor)):
        if pelis_director[i].lower() == pelis_actor[j].lower():
            contador += 1
print(contador)
