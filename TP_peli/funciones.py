def filtrarXgenero(data,genero):
    peliculas = []
    for fila in data:
        if genero in fila[4]:
            peliculas.append(fila[0])
    return peliculas

def filtrarXactor(data,actor):
    peliculas = []
    for fila in data:
        if actor in fila[1]:
            peliculas.append(fila[0])
    return peliculas

def filtrarXdirector(data,director):
    peliculas = []
    for fila in data:
        if director in fila[2]:
            peliculas.append(fila[0])
    return peliculas

def filtrarXanio(data,anio):
    peliculas = []
    for fila in data:
        if anio == fila[6]:
            peliculas.append(fila[0])
    return peliculas

def filtrarXcompania(data,compania):
    peliculas = []
    for fila in data:
        if compania in fila[5]:
            peliculas.append(fila[0])
    return peliculas
