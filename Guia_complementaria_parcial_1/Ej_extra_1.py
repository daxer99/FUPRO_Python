'''Se ingresa fecha de nacimiento, deben determinar edad'''

fecha = input("Ingrese fecha de nacimiento (dd-mm-aaa): ")
hoy = [16,9,2022]

fecha = fecha.split(sep="-")
for i in range(3):
    fecha[i] = int(fecha[i])

edad = hoy[2] - fecha[2]

if fecha[1]>hoy[1] or (fecha[1]==hoy[1] and fecha[0]>hoy[0]):
    edad=edad-1

print(edad)