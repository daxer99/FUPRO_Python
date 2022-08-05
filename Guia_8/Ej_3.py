import statistics as s

datos = []
c = 0
with open("ECG.txt") as file:
    for fila in file:
        datos.append(int(fila.strip('\t\n')))

media = s.mean(datos)
print("Media: ",media)

umbral = media * 20
for i in range(len(datos)):
    if datos[i]>umbral:
        c=c+1

print("Cantidad de valores que superan el umbral: ",c)