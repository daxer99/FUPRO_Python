'''7. En una competencia de salto en alto compiten 20 atletas de diferentes países. Cada atleta realiza 5 saltos en la competencia. 
Escriba un programa Python que haga lo siguiente:
a) Por cada atleta  ingresar inicialmente su número asignado y cada una de las marcas. 
b) Informar el  ganador de la competencia (quien saltó más alto) y la marca lograda. 
c) ¿Cuántos atletas superaron la marca de 3 mts?
d) ¿ Quién registro la menor marca y en qué número de salto?'''

menor_marca = 5
salto_menor_marca = 0
atleta_menor_marca = 0
mejor_marca = 0
ganador = 0
superaron_3 = 0
for i in range(20):
    cod = int(input('Ingrese numero de atleta: '))
    contador = 0
    for j in range(5):
        marca = float(input('Ingrese marca de salto (mts): '))
        if marca > 3:
            contador+=1 
        
        if marca > mejor_marca:
            mejor_marca = marca
            ganador = cod
        
        if marca < menor_marca:
            menor_marca = marca
            salto_menor_marca = j+1
            atleta_menor_marca = i+1
        
    if contador > 1:
        superaron_3 +=1 
print(ganador,mejor_marca)
print(superaron_3)
print(atleta_menor_marca,salto_menor_marca)
