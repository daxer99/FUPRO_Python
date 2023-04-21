'''Escriba un código en Python que lea las fechas de nacimiento de un grupo de 50 personas, con el formato dd/mm/aaaa. A continuación ingrese la fecha actual y realice lo siguiente:
    1. Genere una lista con las edades de cada uno de los 50 individuos al día de hoy.
    2. Indique cuántas personas del grupo son mayores de edad (más de 18 años).'''

fechas_nacimiento = []
for i in range(3):
    fecha_nac = input("Ingrese fecha de nacimiento (dd/mm/aaaa): ")
    fechas_nacimiento.append(fecha_nac)

fecha_actual = input("Ingrese fecha actual (dd/mm/aaaa): ")
fecha_actual = fecha_actual.split("/")
dd_actual = int(fecha_actual[0])
mm_actual = int(fecha_actual[1])
aaaaa_actual = int(fecha_actual[2])

edades = []
for fecha in fechas_nacimiento:
    fecha = fecha.split("/")
    dd_nac =int(fecha[0])
    mm_nac = int(fecha[1])
    aaaa_nac = int(fecha[2])
    edad = aaaaa_actual-aaaa_nac
    if mm_nac > mm_actual:
        edad = edad - 1
    elif mm_nac == mm_actual:
        if dd_nac > dd_actual:
            edad = edad - 1
    edades.append(edad)

print(edades)
print(len([i for i in range(len(edades)) if edades[i]>17]),"personas son mayores de edad")