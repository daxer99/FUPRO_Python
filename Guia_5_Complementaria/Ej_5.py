''' 5. Se ingresan por pantalla los siguientes datos de un grupo de pacientes de un centro médico:
Nombre, DNI, Sexo (M o F), Obra Social y edad. Si un paciente no tiene Obra Social se ingresa “---“. Determine e informe:
a) El % de mujeres del grupo.
b) El número de pacientes menores a 45 años.
c) Muestre solo apellido, nombre y DNI de los pacientes cuya obra social es IOSPER.'''

datos = []
cant_mujeres = 0
cant_menores_45 = 0

nombre = input('Ingrese nombre, 0 para terminar: ')
while nombre != '0':
    dni = input('Ingrese dni: ')
    sexo = input('Ingrese sexo: ')
    os = input('Ingrese OS: ')
    edad = int(input('Ingrese edad: '))
    datos.apend([nombre,dni,sexo,os,edad])

    if sexo.upper() == 'F':
        cant_mujeres += 1
    if edad < 45:
        cant_menores_45 += 1

    nombre = input('Ingrese nombre, 0 para terminar: ')

#A
print(round(cant_mujeres/len(datos)*100,1),'% es el porcentaje de mujeres')
#B
print('El total de menores de 45 años es de',cant_menores_45)
#C
print('Pacientes con IOSPER')
for i in range(len(datos)):
    if datos[i][3].upper() == 'IOSPER':
        print(datos[i][0],datos[i][1])