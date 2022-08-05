'''Escriba un programa que pida un número entero mayor que cero y calcule su factorial.'''

numero = int(input('Ingrese numero: \n'))
factorial = 1

if numero == 0:
    factorial = 1
else:
    for i in range(1,numero+1):
        factorial = factorial * i

print('El factorial de', numero, 'es', factorial)