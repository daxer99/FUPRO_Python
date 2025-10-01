notas = [[None]*40 for i in range(30)]
print(notas)
with open('notas.txt') as file:
    for f in file:
        alumno,materia,calificacion = f.split('	')
        alumno = int(alumno)
        materia = int(materia)
        calificacion = int(calificacion)
        if notas[alumno-1][materia-1] == None:
            notas[alumno - 1][materia - 1] = calificacion
        elif notas[alumno-1][materia-1] >= 6:
            notas[alumno - 1][materia - 1] = calificacion
