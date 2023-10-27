'''El archivo alumnos.txt contiene el dni,nombre, apellido y 3 notas correspondientes a las evaluaciones realizadas por un grupo de estudiantes durante el cursado
de la asignatura. Los campos en el archivo se encuentran separados por coma. Se solicita que:
a) Lea el archivo y calcule la nota final de cada alumno para la asignatura. La nota final es el resultado del promedio entre las 3 notas obtenidas durante el cursado.
b) Defina la condicion final de cada alumno: Libre: nota final menor a 60. Regular: nota final mayor o igual que 60 y las 3 evaluaciones con nota mayor o igual que 60. Promocionado: nota final mayor o igual a 80 y las 3 evaluaciones con nota mayor o igual que 75. Emplee una funcion para obtener la condicion final de cada alumno.
c) Actualice el archivo alumnos.txt incorporando los campos Nota final y Condicion Final con sus respectivos datos.  '''

import statistics as s

def calcular_nota_final(lista_notas):
    return round(s.mean(lista_notas),2)

def calcular_condicion_final(lista_notas):
    nota_final = calcular_nota_final(lista_notas)
    if nota_final >= 80 and lista_notas[0] > 75 and lista_notas[1] > 75 and lista_notas[2] > 75:
        return "Promocionado"
    elif 60<=nota_final<80 and lista_notas[0] > 59 and lista_notas[1] > 59 and lista_notas[2] > 59:
        return "Regular"
    else:
        return "Libre"

data = []
nota_final = []
condicion_final = []
with open("alumnos.txt") as file:
    header = file.readline()
    header = header.strip("\n")
    for fila in file:
        f = fila.split(",")
        data.append([f[0],f[1],f[2],int(f[3]),int(f[4]),int(f[5])])

for i in range(len(data)):
    nota_final.append(calcular_nota_final(data[i][3:]))
    condicion_final.append(calcular_condicion_final(data[i][3:]))

with open("alumnos_2.txt","w") as file:
    file.write(header+",Nota Final, Condicion Final\n")
    for i in range(len(data)):
        file.write(data[i][0]+","+data[i][1]+","+data[i][2]+","+str(data[i][3])+","+str(data[i][4])+","+str(data[i][5])+","+str(nota_final[i])+","+condicion_final[i]+"\n")
