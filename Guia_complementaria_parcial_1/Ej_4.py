'''4. Se lee el código de un paciente y luego los 30 valores consecutivos de concentración de glucosa en sangre registrados en ayunas durante un mes. 
Mediante un programa se desea determinar cuántas veces supero el paciente el umbral de 110 mg/dl y cuál fue la mayor diferencia entre registros de días 
consecutivos. '''

import random as r
contador = 0
mayor_diferencia_registros = 0
glucosa_anterior = 90
cod = input('Ingrese codigo paciente: ')
for i in range(30):
    glucosa = r.randint(80, 130)
    
    if glucosa > 110:
        contador+=1
    
    if abs(glucosa - glucosa_anterior) > mayor_diferencia_registros:
        mayor_diferencia_registros = abs(glucosa-glucosa_anterior)
    
    glucosa_anterior = glucosa

print('El paciente', cod,'supero',contador,'veces el umbral de 110 mg/dl')
print('la mayor diferencia entre registros de días consecutivos fue de',mayor_diferencia_registros)   
