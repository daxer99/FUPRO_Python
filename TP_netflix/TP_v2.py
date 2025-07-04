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
# series_cortas = []
# for fila in netflix_data_series:
#     season = fila[8].split(' ')
#     season = int(season[0])
#     if season < 5:
#         series_cortas.append(fila[1])
# series_cortas_imdb = []
# for i in range(len(series_cortas)):
#     for j in range(len(series_imdb_data)):
#         if series_cortas[i].lower() == series_imdb_data[j][0].lower():
#             series_cortas_imdb.append([series_cortas[i],series_imdb_data[j][2]])
# ordenada = sorted (series_cortas_imdb,key=lambda x:x[1],reverse=True)
# with open('top_5_series_cortas_netflix.csv', 'w') as file:
#     file.write('Titulo,Puntuacion\n')
#     for i in range(5):
#         file.write(ordenada[i][0]+','+ordenada[i][1]+'\n')

#Punto 3
# netflix_movies_90s = []
# for i in range(len(netflix_data_peliculas)):
#     if 1989<int(netflix_data_peliculas[i][6])<2000:
#             netflix_movies_90s.append([netflix_data_peliculas[i][1],netflix_data_peliculas[i][6]])
# netflix_movies_90s_imdb = []
# for i in range(len(netflix_movies_90s)):
#     for j in range(len(movies_imdb_data)):
#         if netflix_movies_90s[i][0].lower() == movies_imdb_data[j][0].lower():
#             netflix_movies_90s_imdb.append([netflix_movies_90s[i][0],netflix_movies_90s[i][1],movies_imdb_data[j][2]])
# ordenada = sorted(netflix_movies_90s_imdb,key=lambda x:x[2],reverse=True)
# with open("top10_1990_1999_movies.csv",'w') as file:
#     file.write('Titulo;Año;Puntuacion\n')
#     for i in range(10):
#         file.write(ordenada[i][0]+';'+ordenada[i][1]+';'+ordenada[i][2]+'\n')

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

# '''¿En qué año se añadieron más series a la plataforma?¿Cuántas fueron?
# ¿Cuántas películas del universo ‘Star Wars’ se encuentran en la plataforma?
# ¿En cuántas películas Robert De Niro y Joe Pesci comparten elenco?
# '''

#Punto 5
# anios = []
# for i in range(len(netflix_data_series)):
#     year = netflix_data_series[i][5].strip(' ').split(',')
#     if year[1].strip(' ') not in anios:
#         anios.append(year[1].strip(' '))
#
# cantidad_series_aniadidas_x_anio = []
# for i in range(len(anios)):
#     cantidad_series_aniadidas_x_anio.append([anios[i],len(filtrarXanioAñadida(netflix_data_series,anios[i]))])
# ordenada = sorted(cantidad_series_aniadidas_x_anio,key=lambda x: x[1],reverse=True)
# print(ordenada[0])

#Punto 6
# naruto_movies = []
# for fila in netflix_data_peliculas:
#     if 'naruto' in fila[1].lower():
#         naruto_movies.append(fila)
# print(len(naruto_movies))

#Punto 7
# contador = 0
# pelis_deniro = filtrarXactor(netflix_data_peliculas,'Robert De Niro')
# pelis_pesci = filtrarXactor(netflix_data_peliculas,'Joe Pesci')
# for i in range(len(pelis_deniro)):
#     for j in range(len(pelis_pesci)):
#         if pelis_deniro[i] == pelis_pesci[j]:
#             contador+=1
# print(contador)

#Defensa

#1 Cuantas comedias románticas hay en el top 1000 de peliculas
# c = 0
# for fila in movies_imdb_data:
#     if 'comedy' in fila[1].lower() and 'romance' in fila[1].lower():
#         c+=1
# print(c)

#2 cuantas series se produjeron en mas de 2 paises
# c = 0
# for fila in netflix_data_series:
#     paises = fila[4].split(',')
#     paises = len(paises)
#     if paises > 2:
#         c+=1
# print(c)

#3 cuantas peliculas del genero action tienen una duración mayor al promedio de todas las películas de este género
# import statistics as s
# peliculas_action_duracion = []
# for fila in netflix_data_peliculas:
#     if 'action' in fila[9].lower():
#         dur = fila[8].split(' ')
#         dur = int(dur[0])
#         peliculas_action_duracion.append(dur)
# promedio_duracion = s.mean(peliculas_action_duracion)
# c = 0
# for i in range(len(peliculas_action_duracion)):
#     if peliculas_action_duracion[i]>promedio_duracion:
#         c+=1
# print(c)

#4 En cuantas peliculas dirigidas por Martin Scorsese actua Leonardo DiCaprio
pelis_director = filtrarXdirector(netflix_data_peliculas,'Martin Scorsese')
pelis_actor = filtrarXactor(netflix_data_peliculas,'Leonardo DiCaprio')
comun =[]

for i in range(len(pelis_director)):
    for j in range(len(pelis_actor)):
        if pelis_director[i].lower() == pelis_actor[j].lower():
            comun.append(pelis_director[i])
print(comun)