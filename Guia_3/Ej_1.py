'''Escriba un programa en Python donde el usuario ingrese un número natural positivo y muestre por consola
todos los valores impares desde 1 hasta el número ingresado.'''

numero = int(input("Ingrese numero natural: "))

i = 1
while i <=numero:
    if i%2 !=0:
        print(i)
    i+=1