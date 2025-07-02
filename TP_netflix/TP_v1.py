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

