'''4. Se lee el código de un paciente y luego los 30 valores consecutivos de concentración de glucosa en sangre registrados en ayunas durante un mes.
Mediante un programa se desea determinar cuántas veces supero el paciente el umbral de 110 mg/dl y cuál fue la mayor diferencia entre registros de días consecutivos. '''

import random

glu_mas_110 = 0
glucosa_anterior = 90
diff_glucosa = 0
id = input('Ingrese codigo de paciente: ')
for i in range(30):
    glucosa = random.randint(80,125)

    if abs(glucosa-glucosa_anterior) > diff_glucosa:
        diff_glucosa = abs(glucosa-glucosa_anterior)

    if glucosa > 110:
        glu_mas_110+=1
    glucosa_anterior = glucosa

print('El paciente', id,'supero',glu_mas_110,'veces el umbral de 110mg/dl')
print('La mayor diferencia entre dias consecutivos fue de',diff_glucosa,'mg/dl')