"""
Diseñe e implemente un programa en Python en donde se ingrese un número e informe: a) si es par o impar; b) si es múltiplo
de 5 y 3 a la vez.
"""

numero = int(input('Ingrese número: '))

# A
if numero % 2 == 0:
    print(numero, 'es par')
else:
    print(numero, 'es impar')

# B
if numero % 3 == 0 and numero % 5 == 0:
    print(numero, 'es multiplo de 3 y 5')
elif numero % 3 == 0:
    print(numero, 'es multiplo de 3')
elif numero % 5 == 0:
    print(numero, 'es multiplo de 5')
else:
    print(numero, 'no es multiplo de 3 y 5')