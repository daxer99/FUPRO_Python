nombres = []
apellidos = []
mail = "@fiuner.edu.ar"

with open('personal.txt','r') as file:
    datos = file.readlines()
    nombres.append(datos)
    print(type(datos))

# with open('personal.txt','r') as file:
#     for fila in file:
#         linea = fila.split(sep=" ")
#         nombres.append(linea[0])
#         apellidos.append(linea[1])
#
# for i in range(len(apellidos)):
#     apellidos[i] = apellidos[i].strip("\n")
#
# with open("correos.txt","w") as file:
#     for i in range(len(nombres)):
#         file.write(nombres[i][0].lower()+apellidos[i].lower()+mail)
#         file.write("\n")