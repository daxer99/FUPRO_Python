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
