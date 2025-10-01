''' Leer el dni y las calificaciones (una calificación por alumno) de un grupo de alumnos que asistieron a una evaluación parcial de Fundamentos de Programación y almacenarlos en una lista. Los datos finalizan con el dni 0. Se desea obtener como información de salida:

a. Un listado de los DNI de los alumnos aprobados.


b. Las 2 mayores calificaciones y los DNI de los alumnos que las obtuvieron.'''

dnis = []
notas = []

dni = int(input('Ingrese DNI, 0 para terminar: '))
while dni != 0:
    dnis.append(dni)
    nota = int(input('Ingrese nota: '))
    notas.append(notas)
    dni = int(input('Ingrese DNI, 0 para terminar: '))

dnis_aprobados = []
dni_mejor_1 = 0
dni_mejor_2 = 0
mejor_nota_1 = 0
mejor_nota_2 = 0
for i in range (len(dnis)):
    if notas[i] >=6:
        dnis_aprobados.append(dnis[i])

    if notas[i] > mejor_nota_1:
        mejor_nota_2 = mejor_nota_1
        dni_mejor_2 = dni_mejor_1
        mejor_nota_1 = notas[i]
        dni_mejor_1 = dnis[i]
    elif notas[i] > mejor_nota_2:
        mejor_nota_2 = notas[i]
        dni_mejor_2 = dnis[i]

print(dnis_aprobados)

