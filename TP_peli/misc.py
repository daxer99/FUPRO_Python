from funciones import filtrarXdirector,filtrarXanio,filtrarXcompania,filtrarXactor,filtrarXgenero
def lista_unica(lista):
    lista_unica = []
    for elemento in lista:
        if elemento not in lista_unica:
            lista_unica.append(elemento)
    return lista_unica

data = []
filename = "tmdb_movies_data.csv"
with open(filename) as file:
    header = file.readline()
    for f in file:
        fila = f.split(sep=",")
        data.append([fila[0],fila[1].split(sep="|"),fila[2].split(sep="|"),int(fila[3]),fila[4].split(sep="|"),
                    fila[5].split(sep="|"),int(fila[6]),float(fila[7]),float(fila[8])])


# print(len(filtrarXgenero(data,"Documentary")))

cont = 0
for fila in data:
    if "Romance" in fila[4] and "Comedy" in fila[4] and fila[6]==1975:
        cont +=1
print(cont)