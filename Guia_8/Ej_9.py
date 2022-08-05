import sys

filename = "CP.csv"
# filename = input("Ingrese nombre de archivo a leer: ")

m = []
cpx = []
cpy = []

# Sin exception
with open(filename) as file:
    for f in file:
        fila = f.split(sep=",")
        m.append([int(fila[i]) for i in range(len(fila))])

# Con exception
# try:
#     file = open(filename)
# except:
#     print("El archivo ingresado no es correcto")
# else:
#     for f in file:
#         fila = f.split(sep=",")
#         m.append([int(fila[i]) for i in range(len(fila))])

# Con exception y contador
# intentos = 0
# while intentos < 3:
#     try:
#         file = open(filename)
#         for f in file:
#             fila = f.split(sep=",")
#             m.append([int(fila[i]) for i in range(len(fila))])
#         break

#     except:
#         print("El archivo ingresado no es correcto!!\n")
#         filename = input("Ingrese nombre de archivo a leer: ")
#         intentos = intentos +1
# if(intentos == 3):
#     print("Maximos intentos realizados")
#     sys.exit()


for i in range(len(m)):
    valor_cpx = (433 / 2) * ((m[i][2] + m[i][3] - m[i][0] + m[i][1]) / sum(m[i]))
    cpx.append(round(valor_cpx, 2))

for i in range(len(m)):
    valor_cpy = (238 / 2) * ((m[i][0] + m[i][2] - m[i][1] + m[i][3]) / sum(m[i]))
    cpy.append(round(valor_cpy, 2))

with open("Desplazamiento.txt", "w") as file:
    for i in range(len(cpx)):
        file.write(str(cpx[i]) + "\t" + str(cpy[i]))
        file.write("\n")
