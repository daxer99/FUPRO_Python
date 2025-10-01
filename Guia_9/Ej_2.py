# -*- coding: utf-8 -*-
"""
En el archivo “clinica.txt” se encuentran almacenadas las visitas
durante los tres últimos años a un centro de salud de la ciudad
de Paraná, que posee varios consultorios: pediatría, ginecología,
cardiología, etc., el archivo tiene 4 datos por línea separados
por coma: código del servicio (número entero entre 1 y 15),
nombre del servicio (string), fecha (dd/mm/aaaa),
cantidad de visitas (número entero).
Por razones de simplicidad se necesita dividir la información
en un archivo por año: “clinica2020.txt”, “clinica2021.txt”,
“clinica2022.txt”. Separe la información en un archivo por año.
El archivo “clinica2022.txt” ya fue creado por lo que debe
agregar la nueva información que se encuentra en “clinica.txt”
sin perder los datos que contiene. Luego el usuario debe
ingresar un año, el programa debe validar que el año ingresado
es correcto (2020, 2021, 2022) y volver a dar la oportunidad
de ingresarlo si es incorrecto. Para el año ingresado determine:

a- Cuáles fueron los tres servicios más requeridos durante todo el año
b- El mes que más visitas tuvo
c- Cuántos pacientes visitaron la clínica en verano y cuántos en invierno
d- Promedio de pacientes por día para el servicio de pediatría en julio
e-  Cuáles fueron los dos servicios más requeridos en el verano
f- Cuántos pacientes visitaron la clínica en todo el año
"""
f2020 = open("clinica2020.txt", 'w')
f2021 = open("clinica2021.txt", 'w')
f2022 = open("clinica2022.txt", 'a')
with open("clinica.txt") as f:
    for fila in f:
        codigo, nombre, fecha, cantidad = fila.split(',')
        anio = int(fecha[6:])
        if anio == 2020:
            f2020.write(fila)
        if anio == 2021:
            f2021.write(fila)
        if anio == 2022:
            f2022.write(fila)

f2020.close()
f2021.close()
f2022.close()

anio = int(input("ingrese un año: "))
while 2020 > anio or anio > 2022:
    anio = int(input("Error! el año debe ser 2020,2021 o 2022, vuleva a ingresar"))

filename = "clinica" + str(anio) + ".txt"
Servicio_mes = [[0] * 12 for x in range(15)]
Servicio_nombre = [None] * 15
Pacientes_Verano = 0
Pacientes_Invierno = 0
Servicio_verano = [0] * 15
with open(filename) as f:
    for fila in f:
        codigo, nombre, fecha, cantidad = fila.split(',')
        mes = int(fecha[3:5])
        Servicio_mes[int(codigo) - 1][mes - 1] += int(cantidad)
        Servicio_nombre[int(codigo) - 1] = nombre
        dia = int(fecha[0:2])
        if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
            Pacientes_Verano += int(cantidad)
            Servicio_verano[int(codigo) - 1] += int(cantidad)
        if (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
            Pacientes_Invierno += int(cantidad)

servicios = [(x + 1, sum(Servicio_mes[x])) for x in range(15)]
servicios.sort(key=lambda x: x[1], reverse=True)
print("los tres servicios más requeridos: ",
      [(servicios[x][0], Servicio_nombre[servicios[x][0] - 1]) for x in (0, 1, 2)])

suma_meses = [0] * 12
for mes in range(12):
    for s in range(15):
        suma_meses[mes] += Servicio_mes[s][mes]
print("El mes que más visitas tuvo: ", suma_meses.index(max(suma_meses)) + 1)
print("pacientes visitaron la clínica en verano: ", Pacientes_Verano)
print("pacientes visitaron la clínica en invierno: ", Pacientes_Invierno)
print("Promedio de pacientes en pediatría en julio: ", Servicio_mes[2 - 1][7 - 1] // 31)
Servicio_verano_ordenado = sorted(Servicio_verano, reverse=True)
primero = Servicio_verano.index(Servicio_verano_ordenado[0])
segundo = Servicio_verano.index(Servicio_verano_ordenado[1])
print("los dos servicios más requeridos en el verano: ",
      primero + 1, Servicio_nombre[primero], " y ", segundo + 1,
      Servicio_nombre[segundo])
print("Cantidad de pacientes que visitaron la clínica en todo el año: ",
      sum(suma_meses))