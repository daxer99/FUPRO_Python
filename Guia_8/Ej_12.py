'''El archivo operaciones_aeroportuarias.csv contiene informacion sobre la cantidad de llegadas y partidas de vuelos de 10 aeropuertos de Estados Unidos.
La informacion esta organiza de la siguiente manera: en la primer fila se encuentra el codigo del aeropuerto,
en la segunda fila 11 valores numericos que indican la cantidad de salidas anuales de cada aeropuerto desde 2004 a 2014 y
en la tercer fila 11 valores numericos que indican la cantidad de llegadas anuales de cada aeropuerto desde 2004 a 2014. Se desea que:
a) organice la informacion de manera adecuada.
b) Diseñe e implemente una funcion que calcule la diferencia porcentual que existe entre las llegadas de cada aeropuerto de 2004 y 2014.
c) ¿Que aeropuerto presenta una mayor diferencia porcentual entre las llegadas de 2004 y 2014?.
d) ¿Que aeropuerto presenta un mayor promedio de salidas a lo largo de todos los años?¿con que valor?.
e) ¿Cual fue el año de mayor salidas entre todos los aeropuertos? ¿con que cantidad? ¿A que aeropuerto pertenece ese valor?'''

import statistics as s
def diferencia_porcentual(a,b):
    return round(abs(b-a)/a*100,2)

#B
def diferencia_porcentual_llegadas_aeropuertos_2004_2014(matriz):
    diff = []
    for aeropuerto in matriz:
        diff.append(diferencia_porcentual(aeropuerto[2][0],aeropuerto[2][-1]))
    return diff

#A
airports = []
llegadas = []
salidas = []

with open("operaciones_aeroportuarias.csv") as file:
    file = list(file)
    for i in range(0,len(file),3):
        airports.append(file[i].strip('\n'))
        salidas.append(file[i + 1].strip('\n').split(','))
        llegadas.append(file[i+2].strip('\n').split(','))

for i in range(len(llegadas)):
    for j in range(len(llegadas[0])):
        llegadas[i][j] = int(llegadas[i][j])
        salidas[i][j] = int(salidas[i][j])

data = list(zip(airports,salidas,llegadas))

#C
diferencias = diferencia_porcentual_llegadas_aeropuertos_2004_2014(data)
indice_aeropuerto_max_diff = diferencias.index(max(diferencias))
aeropuerto_max_diff = data[indice_aeropuerto_max_diff][0]
print("El aeropuerto que presenta una mayor diferencia porcentual entre las llegadas de 2004 y 2014 es:",aeropuerto_max_diff)

#D
promedios = []
for aero in data:
    promedios.append(round(s.mean(aero[1])))
indice_aeropuerto_max_prom_salidas = promedios.index(max(promedios))
aeropuerto_max_prom_salidas = data[indice_aeropuerto_max_prom_salidas][0]
print("El aeropuerto que presenta mayor promedio de salidas a lo largo de todos los años es:",aeropuerto_max_prom_salidas,"con un valor de",promedios[indice_aeropuerto_max_prom_salidas])

#E
mayor_salidas = 0
anio_mayor_salidas = 0
aeropuerto_anio_mayor_salidas = ''

for aero in data:
    for i in range(len(aero[2])):
        if aero[2][i]> mayor_salidas:
            mayor_salidas = aero[2][i]
            anio_mayor_salidas = i+2004
            aeropuerto_anio_mayor_salidas = aero[0]
print("El año de mayor salidas entre todos los aeropuertos fue:", anio_mayor_salidas,"con",mayor_salidas,"desde el aeropuerto",aeropuerto_anio_mayor_salidas)