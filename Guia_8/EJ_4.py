def plural(string):
    s = ""
    if string[-1].lower() in ('a', 'e', 'i', 'o', 'u'):
        s = string + "s"
    else:
        s = string + "es"
    return s


palabras = []

with open("PALABRAS.txt") as file:
    for fila in file:
        palabras.append(fila.strip('\t\n'))

with open("palabras_plural.txt", "w") as file:
    for i in palabras:
        file.write(plural(i))
        file.write("\n")