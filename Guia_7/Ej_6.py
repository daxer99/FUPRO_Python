'''6. Un grupo de investigación analiza el comportamiento de 65 pacientes hospitalizados y afectados por COVID19.
Para ello se ingresan el número de paciente y luego los valores de presión de oxígeno en sangre registrados para ese paciente durante 7 días (una medición por día).

a) Almacene la información ingresada en una lista.

b) Calcule mediante una función  cuántos pacientes tuvieron hipoxemia (presión de oxígeno inferior a 72) durante 2 o más días.
Escriba el programa en Python que calcule e informe los resultados.'''
import random

def cant_pacientes_hipoxemia(matrix):
    c = 0
    cant = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < 72:
                c+=1
        if c>=2:
            cant+=1
        c=0
    return cant

rows, cols = 2,7
matrix = [([0]*cols) for i in range(rows)]

for i in range(len(matrix)):
    cod_paciente = int(input("Ingrese cod de paciente (1-65): "))
    for j in range(len(matrix[0])):
        medicion = random.randint(65,99)
        #medicion = int(input("Para el paciente "+str(cod_paciente +1)+" ingrese la medicion "+str(j+1)+":"))
        matrix[cod_paciente-1][j] = medicion

print()
print("Cantidad pacientes con hipoxemia: ",cant_pacientes_hipoxemia(matrix))


