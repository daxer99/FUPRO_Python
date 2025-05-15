'''1. En una olimpíada estudiantil compiten N alumnos en 3 pruebas (1: matemáticas, 2: física y 3: computación).
Se ingresan por cada inscripto el DNI y su número asignado para la competencia (entre 1 y N).
Luego, sin orden alguno, se van ingresando ternas con los puntajes de cada prueba:
nro de participante, código de actividad (1: matemáticas, 2: física y 3: computación), puntaje en la actividad.
Escriba un algoritmo que determine:
a) El DNI del ganador de la competencia y el puntaje total obtenido.
b) El DNI del estudiante que ocupó el 2do lugar y su puntaje.
c) ¿Qué puntaje obtuvo en Computación el ganador de la competencia?'''

N = int(input("Ingrese la cantidad de alumnos: "))
M = [[0]*5 for i in range(N)]

while True:
    DNI = input('Ingrese DNI, 0 para terminar: ')
    if DNI == '0':
        break
    id = int(input('Ingrese nro de participante: '))
    cod_act = int(input("Ingrese codigo de actividad: "))
    puntaje = int(input("Ingrese puntaje: "))

    M[id-1][0] = DNI
    M[id-1][cod_act] = puntaje

#Sumar los puntajes
for i in range (len(M)):
    M[i][4] = sum(M[i][1:3])
#Ordenar lista segun los puntajes
M_ord = sorted(M, key= lambda x:x[4],reverse=True)
print("El ganador es:",M[0][0], "con",M[0][4],"puntos")
print("El segundo lugar es:",M[1][0], "con",M[1][4],"puntos")
print("Puntaje de computacion ganador:",M[0][3])