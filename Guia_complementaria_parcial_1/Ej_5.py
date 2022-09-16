''' Se ingresan por pantalla los siguientes datos de un grupo de pacientes
de un centro médico: Nombre, DNI, Sexo (M o F), Obra Social y edad.
Si un paciente no tiene Obra Social se ingresa “---“. Determine e informe:
a) El % de mujeres del grupo.
b) El número de pacientes menores a 45 años.
c) Muestre solo apellido, nombre y DNI de los pacientes cuya obra social es IOSPER.'''

pacientes = []

apellido = input("Ingrese apellido: ")
nombre = input("Ingrese nombre: ")
dni = int(input("Ingrese dni: "))
sexo = input("Ingrese sexo: ")
os = input("Ingrese OS: ")
edad = int(input("Ingrese edad: "))

while edad !=999:
    pacientes.append([apellido,nombre,dni,sexo,os,edad])

    apellido = input("Ingrese apellido: ")
    nombre = input("Ingrese nombre: ")
    dni = int(input("Ingrese dni: "))
    sexo = input("Ingrese sexo: ")
    os = input("Ingrese OS: ")
    edad = int(input("Ingrese edad: "))

#a
f = 0
for i in range(len(pacientes)):
    if pacientes[i][3] == 'F':
        f +=1
print("El porcentage de mujeres es del ",f/len(pacientes)*100," %")

#b
e = 0
for i in range(len(pacientes)):
    if pacientes[i][5] < 45:
        e +=1
print("Cantidad menores de 45 años: ",e)

#c
print()
print("Lista IOSPER")
for i in range(len(pacientes)):
    if pacientes[i][4] == "IOSPER":
        print(pacientes[i][0], pacientes[i][1], pacientes[i][2])
