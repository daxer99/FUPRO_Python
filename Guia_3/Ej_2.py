'''Escriba un programa en Python donde el usuario ingrese números naturales, se sumen y se muestre el resultado por pantalla. Para que el usuario deje de añadir números a la suma debe ingresar el valor -1'''

numero = int(input('Ingrese numero natural, -1 para finalizar: '))
suma = 0

while numero != -1:
    suma = suma + numero
    print('Suma =', suma)
    numero = int(input('Ingrese numero natural, -1 para finalizar: '))

print('Suma =', suma)