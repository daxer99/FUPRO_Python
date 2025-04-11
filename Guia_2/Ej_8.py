'''8.  Escriba un programa que permita determinar la condición final de un alumno en una asignatura que tiene las siguientes condiciones:

Regular: Asistencia a clases 75%, notas de los parciales con promedio mayor o igual a 60% y ninguna de las menores a 50%.
Promocional: Asistencia a clases 75%, notas de los parciales con promedio mayor o igual a 75% y ninguna de las menores a 60%.
Pida al usuario todos los datos necesarios para establecer la condición y en el caso de promoción calcule la nota final en la asignatura si la misma se establece realizando un promedio.'''

asistencia = int(input("Ingrese % de asistencia: "))
nota1 = int(input("Ingrese nota 1: "))
nota2 = int(input("Ingrese nota 2: "))
nota_promedio = (nota1+nota2)/2

if asistencia >= 75:
    if nota_promedio >=75:
        if nota1 >=60 and nota2 >=60:
            print("Condicion: Promocion")
    elif nota_promedio >=60:
        if nota1 >=50 and nota2 >=50:
            print("Condicion: Regular")
    else:
        print("Condicion: Libre")
else:
    print("Condicion: Libre")
