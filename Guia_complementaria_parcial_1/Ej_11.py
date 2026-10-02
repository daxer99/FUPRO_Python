'''11. En una cohorte de 25 estudiantes se registran las calificaciones obtenidas en 4 evaluaciones a lo largo del semestre.
Para cada estudiante se ingresa:
número de DNI del estudiante
luego sus 4 calificaciones (valores entre 1 y 10)
Se pide desarrollar un programa que:
a) Calcule el promedio de cada estudiante y lo informe junto con su condición: promocional, regular o libre por evaluaciones.
b) Informe cuántos estudiantes aprobaron (promedio ≥ 6).
c) Determine el número de DNI del estudiante con mayor promedio.
d) Indique cuántos estudiantes tuvieron al menos una nota inferior a 3.'''

estudiantes_menor_3 = 0
mejor_promedio = 0
est_mejor_promedio = 0
aprobados = 0
    
for i in range(25):
    dni = input('Ingrese DNI de estudiante: ')
    suma = 0
    contador = 0
    for j in range(4):
        p = str(j+1)
        nota = int(input('Ingrese nota '+p+':'))
        suma += nota
        if nota < 3:
            contador+=1
    promedio = suma/4
   
    if 0<promedio<6:
        print(promedio,'libre')
    elif 6<=promedio<8:
        print(promedio,'regular')
    else:
        print(promedio,'promocional')
    
    if promedio > mejor_promedio:
        mejor_promedio = promedio
        est_mejor_promedio = dni
        
    if contador > 0:
        estudiantes_menor_3 +=1 
    
    if promedio > 6:
        aprobados +=1

print(aprobados)
print(est_mejor_promedio)
print(estudiantes_menor_3)
