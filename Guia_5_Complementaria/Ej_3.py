'''3. Se leen por consola los registros de infectados y fallecidos en el año 2020
de 15 países (nombre del país, número infectados, número fallecidos) y se los almacena en una lista.
a) Calcule e informe la proporción de fallecidos respecto de infectados del país 5 en 2020.
b) Informe cuántos países tuvieron % de mortalidad superior al 3% en 2020 y los nombres de los mismos.
c) Calcule e informe el total de muertes de todo 2020.'''

datos =[]
for i in range(15):
    nom = input()
    infectados = int(input())
    muertos = int(input())
    datos.append([nom,infectados,muertos])
#A
prop_muertos_pais_5 = datos[4][2]/datos[4][1]*100
#B
paises_mortalidad_mayor_3 = []
for i in range(len(datos)):
    if (datos[i][2]/datos[i][1]*100) > 3:
        paises_mortalidad_mayor_3.append(datos[i][0])
print("La cantidad de paises que superan una mortalidad del 3% son",len(paises_mortalidad_mayor_3))
print(paises_mortalidad_mayor_3)
#C
total_muertes = 0
for i in range(len(datos)):
    total_muertes += datos[i][2]
