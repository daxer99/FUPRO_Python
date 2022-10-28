'''En el archivo “clinica.txt” se encuentran almacenadas las visitas durante los tres últimos años a un centro de salud de la ciudad de Paraná,
que posee varios consultorios: pediatría, ginecología, cardiología, etc., el archivo tiene 4 datos por línea separados por coma: código del servicio (número entero entre 1 y 15),
nombre del servicio (string), fecha (dd/mm/aaaa), cantidad de visitas (número entero). Por razones de simplicidad se necesita dividir la información en un archivo por año:
“clinica2020.txt”, “clinica2021.txt”, “clinica2022.txt”. Separe la información en un archivo por año. El archivo “clinica2022.txt” ya fue creado por lo que debe agregar la nueva
información que se encuentra en “clinica.txt” sin perder los datos que contiene. Luego el usuario debe ingresar un año, el programa debe validar que el año ingresado es correcto
(2020, 2021, 2022) y volver a dar la oportunidad de ingresarlo si es incorrecto. Para el año ingresado determine:

a- Cuáles fueron los tres servicios más requeridos durante todo el año
b- El mes que más visitas tuvo
c- Cuántos pacientes visitaron la clínica en verano y cuántos en invierno
d- Promedio de pacientes por día para el servicio de pediatría en julio
e-  Cuáles fueron los dos servicios más requeridos en el verano
f- Cuántos pacientes visitaron la clínica en todo el año '''


from operator import itemgetter

#######################################################################################################################
entrada = open("clinica.txt")
salida_2020 = open("clinica_2020.txt","w")
salida_2021 = open("clinica_2021.txt","w")
salida_2022 = open("clinica_2022.txt","w")

lista_2020 = []
lista_2021 = []
lista_2022 = []

for fila in entrada:
    cod_servicio,nombre_servicio,fecha,cantidad_visitas = fila.strip('\n').split(sep=",")
    if int(fecha[6:]) == 2020:
        lista_2020.append([int(cod_servicio),nombre_servicio,fecha,int(cantidad_visitas)])
        salida_2020.write(fila)
    elif int(fecha[6:]) == 2021:
        lista_2021.append([int(cod_servicio), nombre_servicio, fecha, int(cantidad_visitas)])
        salida_2021.write(fila)
    elif int(fecha[6:]) == 2022:
        lista_2022.append([int(cod_servicio), nombre_servicio, fecha, int(cantidad_visitas)])
        salida_2022.write(fila)

entrada.close()
salida_2020.close()
salida_2021.close()
salida_2022.close()
########################################################################################################################
anio = int(input("Ingrese anio (2020,2021,2022) a procesar: "))
while True:
    if anio == 2020:
        break
    elif anio == 2021:
        break
    elif anio == 2022:
        break
    else:
        anio = int(input("Ingrese anio (2020,2021,2022) a procesar: "))
########################################################################################################################
suma_servicios = [0 for i in range(15)]
servicios = [i for i in range(15)]
suma_meses = [0 for i in range(12)]
meses = [i for i in range(12)]
pacientes_verano = 0
pacientes_invierno = 0
cantidad_visitas_julio = 0
suma_servicios_verano = [0 for i in range(15)]
total_pacientes = 0


if anio == 2020:
    # A
    for i in range(15):
        for j in range(len(lista_2020)):
            if lista_2020[j][0] == i+1:
                suma_servicios[i]+=lista_2020[j][3]
    suma_servicios= list(zip(servicios,suma_servicios))
    servicios_ordenados = sorted(suma_servicios,key=itemgetter(1),reverse = True)
    print("Los tres servicios mas requeridos durante todo el año fueron: ",servicios_ordenados[0][0]+1,servicios_ordenados[1][0]+1,servicios_ordenados[2][0]+1)

    # B
    for i in range(12):
        for j in range(len(lista_2020)):
            fecha = lista_2020[j][2]
            mes = int(fecha[3:5])
            if mes == i+1:
                suma_meses[i]+=lista_2020[j][3]
    suma_meses= list(zip(meses,suma_meses))
    meses_ordenados = sorted(suma_meses,key=itemgetter(1),reverse = True)
    print("El mes ",meses_ordenados[0][0]+1," fue el que mas visitas tuvo con ",meses_ordenados[0][1])

    #C
    for j in range(len(lista_2020)):
        fecha = lista_2020[j][2]
        dia = int(fecha[0:2])
        mes = int(fecha[3:5])
        if mes in (1,2,3):
            season = 'summer'
        elif mes in (7,8,9):
            season = 'winter'

        if (mes == 6) and (dia > 20):
            season = 'winter'
        elif (mes == 12) and (dia > 20):
            season = 'summer'

        if season == 'summer':
            pacientes_verano += lista_2020[j][3]
        elif season == 'winter':
            pacientes_invierno += lista_2020[j][3]

    print("En verano asistieron ",pacientes_verano," pacientes")
    print("En invierno asistieron ",pacientes_invierno," pacientes")

    # D
    for j in range(len(lista_2020)):
        fecha = lista_2020[j][2]
        mes = int(fecha[3:5])
        if mes == 6 and lista_2020[j][1]=="Pediatria":
            cantidad_visitas_julio += lista_2020[j][3]

    print("Promedio de pacientes por día para el servicio de pediatría en julio: ", round(cantidad_visitas_julio/31,2))

    # E
    for i in range(15):
        for j in range(len(lista_2020)):
            fecha = lista_2020[j][2]
            dia = int(fecha[0:2])
            mes = int(fecha[3:5])
            if mes in (1, 2, 3):
                season = 'summer'
            if (mes == 12) and (dia > 20):
                season = 'summer'
            elif (mes == 3) and (dia > 19):
                season = 'autumn'

            if lista_2020[j][0] == i+1 and season == 'summer':
                suma_servicios_verano[i]+=lista_2020[j][3]
    suma_servicios_verano= list(zip(servicios,suma_servicios_verano))
    servicios_verano_ordenados = sorted(suma_servicios_verano,key=itemgetter(1),reverse = True)
    print("Los dos servicios mas requeridos durante el verano fueron: ", servicios_verano_ordenados[0][0] + 1, servicios_verano_ordenados[1][0] + 1)

    # F
    for j in range(len(lista_2020)):
        total_pacientes += lista_2020[j][3]
    print("El total de pacientes que asistió a la clínica fue de ",total_pacientes)
elif anio == 2021:
    # A
    for i in range(15):
        for j in range(len(lista_2021)):
            if lista_2021[j][0] == i+1:
                suma_servicios[i]+=lista_2021[j][3]
    suma_servicios= list(zip(servicios,suma_servicios))
    servicios_ordenados = sorted(suma_servicios,key=itemgetter(1),reverse = True)
    print("Los tres servicios mas requeridos durante todo el año fueron: ",servicios_ordenados[0][0]+1,servicios_ordenados[1][0]+1,servicios_ordenados[2][0]+1)

    # B
    for i in range(12):
        for j in range(len(lista_2021)):
            fecha = lista_2021[j][2]
            mes = int(fecha[3:5])
            if mes == i+1:
                suma_meses[i]+=lista_2021[j][3]
    suma_meses= list(zip(meses,suma_meses))
    meses_ordenados = sorted(suma_meses,key=itemgetter(1),reverse = True)
    print("El mes ",meses_ordenados[0][0]+1," fue el que mas visitas tuvo con ",meses_ordenados[0][1])

    #C
    for j in range(len(lista_2021)):
        fecha = lista_2021[j][2]
        dia = int(fecha[0:2])
        mes = int(fecha[3:5])
        if mes in (1,2,3):
            season = 'summer'
        elif mes in (7,8,9):
            season = 'winter'

        if (mes == 6) and (dia > 20):
            season = 'winter'
        elif (mes == 12) and (dia > 20):
            season = 'summer'

        if season == 'summer':
            pacientes_verano += lista_2021[j][3]
        elif season == 'winter':
            pacientes_invierno += lista_2021[j][3]

    print("En verano asistieron ",pacientes_verano," pacientes")
    print("En invierno asistieron ",pacientes_invierno," pacientes")

    # D
    for j in range(len(lista_2021)):
        fecha = lista_2021[j][2]
        mes = int(fecha[3:5])
        if mes == 6 and lista_2021[j][1]=="Pediatria":
            cantidad_visitas_julio += lista_2021[j][3]

    print("Promedio de pacientes por día para el servicio de pediatría en julio: ", round(cantidad_visitas_julio/31,2))

    # E
    for i in range(15):
        for j in range(len(lista_2021)):
            fecha = lista_2021[j][2]
            dia = int(fecha[0:2])
            mes = int(fecha[3:5])
            if mes in (1, 2, 3):
                season = 'summer'
            if (mes == 12) and (dia > 20):
                season = 'summer'
            elif (mes == 3) and (dia > 19):
                season = 'autumn'

            if lista_2021[j][0] == i+1 and season == 'summer':
                suma_servicios_verano[i]+=lista_2021[j][3]
    suma_servicios_verano= list(zip(servicios,suma_servicios_verano))
    servicios_verano_ordenados = sorted(suma_servicios_verano,key=itemgetter(1),reverse = True)
    print("Los dos servicios mas requeridos durante el verano fueron: ", servicios_verano_ordenados[0][0] + 1, servicios_verano_ordenados[1][0] + 1)

    # F
    for j in range(len(lista_2021)):
        total_pacientes += lista_2021[j][3]
    print("El total de pacientes que asistió a la clínica fue de ",total_pacientes)

if anio == 2022:
    # A
    for i in range(15):
        for j in range(len(lista_2022)):
            if lista_2022[j][0] == i+1:
                suma_servicios[i]+=lista_2022[j][3]
    suma_servicios= list(zip(servicios,suma_servicios))
    servicios_ordenados = sorted(suma_servicios,key=itemgetter(1),reverse = True)
    print("Los tres servicios mas requeridos durante todo el año fueron: ",servicios_ordenados[0][0]+1,servicios_ordenados[1][0]+1,servicios_ordenados[2][0]+1)

    # B
    for i in range(12):
        for j in range(len(lista_2022)):
            fecha = lista_2022[j][2]
            mes = int(fecha[3:5])
            if mes == i+1:
                suma_meses[i]+=lista_2022[j][3]
    suma_meses= list(zip(meses,suma_meses))
    meses_ordenados = sorted(suma_meses,key=itemgetter(1),reverse = True)
    print("El mes ",meses_ordenados[0][0]+1," fue el que mas visitas tuvo con ",meses_ordenados[0][1])

    #C
    for j in range(len(lista_2022)):
        fecha = lista_2022[j][2]
        dia = int(fecha[0:2])
        mes = int(fecha[3:5])
        if mes in (1,2,3):
            season = 'summer'
        elif mes in (7,8,9):
            season = 'winter'

        if (mes == 6) and (dia > 20):
            season = 'winter'
        elif (mes == 12) and (dia > 20):
            season = 'summer'

        if season == 'summer':
            pacientes_verano += lista_2022[j][3]
        elif season == 'winter':
            pacientes_invierno += lista_2022[j][3]

    print("En verano asistieron ",pacientes_verano," pacientes")
    print("En invierno asistieron ",pacientes_invierno," pacientes")

    # D
    for j in range(len(lista_2022)):
        fecha = lista_2022[j][2]
        mes = int(fecha[3:5])
        if mes == 6 and lista_2022[j][1]=="Pediatria":
            cantidad_visitas_julio += lista_2022[j][3]

    print("Promedio de pacientes por día para el servicio de pediatría en julio: ", round(cantidad_visitas_julio/31,2))

    # E
    for i in range(15):
        for j in range(len(lista_2022)):
            fecha = lista_2022[j][2]
            dia = int(fecha[0:2])
            mes = int(fecha[3:5])
            if mes in (1, 2, 3):
                season = 'summer'
            if (mes == 12) and (dia > 20):
                season = 'summer'
            elif (mes == 3) and (dia > 19):
                season = 'autumn'

            if lista_2022[j][0] == i+1 and season == 'summer':
                suma_servicios_verano[i]+=lista_2022[j][3]
    suma_servicios_verano= list(zip(servicios,suma_servicios_verano))
    servicios_verano_ordenados = sorted(suma_servicios_verano,key=itemgetter(1),reverse = True)
    print("Los dos servicios mas requeridos durante el verano fueron: ", servicios_verano_ordenados[0][0] + 1, servicios_verano_ordenados[1][0] + 1)

    # F
    for j in range(len(lista_2022)):
        total_pacientes += lista_2022[j][3]
    print("El total de pacientes que asistió a la clínica fue de ",total_pacientes)