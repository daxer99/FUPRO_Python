'''7- En una competencia de salto en alto compiten 20 atletas de diferentes países.
Cada atleta realiza 5 saltos en la competencia. Escriba un programa Python que haga lo siguiente:
a) Por cada atleta  ingresar inicialmente su número asignado y cada una de las marcas.
b) Informar el  ganador de la competencia (quien saltó más alto) y la marca lograda.
c) ¿Cuántos atletas superaron la marca de 3 mts?
d) ¿ Quién registro la menor marca y en qué número de salto?'''

import random as r

mejor_salto = 0
atleta_mejor_salto = 0
peor_salto = 10
atleta_peor_salto = 0
numero_peor_salto = 0
salto_mas_3_mts = 0
cont = 0

for i in range(20):
    atleta = input('Ingrese ID de atleta: ')
    for j in range(5):
        salto = r.uniform(1.8,3.5)

        if salto > mejor_salto:
            mejor_salto = salto
            atleta_mejor_salto = atleta

        if salto < peor_salto:
            peor_salto = salto
            atleta_peor_salto = atleta
            numero_peor_salto = j+1

        if salto > 3:
            cont+=1

    if cont > 0:
        salto_mas_3_mts+=1
    cont = 0

print('El atleta',atleta_mejor_salto,'gano la competencia con un salto de',mejor_salto,'mts')
print(salto_mas_3_mts,'atletas superaron los 3 mts')
print('El atleta',atleta_peor_salto,'registro la peor marca en el salto',numero_peor_salto)