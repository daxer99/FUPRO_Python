'''10. Para determinar la condición final de los alumnos de un curso de la asignatura Química se ingresa el nombre del alumno, las dos notas de los parciales y la cantidad de trabajos prácticos aprobados. Escriba una función que determine la condición de cada alumno sabiendo que para regularizar la materia debe tener promedio de los parciales mayor a 60 y 5 o más trabajos prácticos aprobados, sino cumple con alguno de estos requisitos estará en condición de libre. Informe un listado con los nombres de los alumnos y su condición final (regular o libre).'''

datos = []

nombre = input("Ingrese nombre completo, 0 para terminar: ")
while nombre !='0':
    n1 = int(input('Ingrese nota del parcial 1: '))
    n2 = int(input('Ingrese nota del parcial 2: '))
    tps_aprobados = int(input('Ingrese cantidad de tps aprobados: '))
    datos.append([nombre,n1,n2,tps_aprobados])

condicion = []
for i in range(len(datos)):
    promedio = (datos[i][1]+datos[i][2])/2
    if promedio > 60 and datos[i][3]>=5:
        condicion.append([datos[i],'Regular'])
    else:
        condicion.append([datos[i], 'Libre'])

for i in range(len(condicion)):
    print(condicion[i])
