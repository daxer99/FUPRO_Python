'''3. Una cooperadora escolar recibe aportes voluntarios y de montos variables de sus alumnos.
La escuela tiene 3 cursos de jardín y desea hacer un análisis de los aportes por curso y por cada uno de los meses del año pasado.
Para ello se leen los datos de cada aporte: Curso, Mes, Monto: donde curso es un número de 1 a 3, mes es un número de 1 a 12 y monto es el valor monetario del aporte; estos datos terminan al ingresar un 0 para el dato curso.
Un mismo alumno puede hacer varios aportes en el año. Se desea informar: a) el total aportado en cada curso en todo el año  b) el total recaudado sumando aportado en los meses de marzo y agosto sin importar el curso.'''

c1 = 0
c2 = 0
c3 = 0
marzo_agosto = 0

curso = int(input("Ingrese curso (1-3): "))
while curso !=0:
    mes = int(input("Ingrese mes (1-12): "))
    monto = float (input("Ingrese monto: "))

    if curso == 1:
        c1 = c1 + monto
    elif curso == 2:
        c2 = c2 + monto
    elif curso == 3:
        c3 = c3 + monto
    else:
        print('Opcion incorrecta de curso')

    if mes == 3 and mes == 8:
        marzo_agosto+=monto

    curso = int(input("Ingrese curso (1-3): "))

print('Recaudacion curso 1:',c1)
print('Recaudacion curso 2:',c2)
print('Recaudacion curso 3:',c3)
print('Recaudacion marzo y agosto:',marzo_agosto)