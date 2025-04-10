'''1. Escriba un programa que escriba la tabla de multiplicar de un número ingresado por el usuario.
El usuario también establece si la tabla se muestra en forma ascendente o descendente.'''

numero = int(input('Ingrese numero para generar tabla de multiplicar: '))
opcion = int(input('Ingrese 1 para mostrar ascendente o 2 para mostrar descendente: '))
print()
if opcion == 1:
    print('Tabla del',numero,'de forma ascendente:')
    for i in range(1,11):
        print(numero,'x',i,'=',numero*i)
elif opcion == 2:
    print('Tabla del', numero, 'de forma descendente:')
    for i in range(10, 0,-1):
        print(numero, 'x', i, '=', numero * i)
else:
    print('Opcion incorrecta')
