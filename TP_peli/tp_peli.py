
#1
data = []
filename = "tmdb_movies_data.csv"
with open(filename) as file:
    header = file.readline()
    for f in file:
        fila = f.split(sep=",")
        data.append([fila[0],fila[1].split(sep="|"),fila[2].split(sep="|"),int(fila[3]),fila[4].split(sep="|"),
                    fila[5].split(sep="|"),int(fila[6]),int(fila[7]),int(fila[8])])

