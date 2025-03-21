'''Escriba un programa que pida tres números y diga si forman una sucesión aritmética o geométrica. Recuerda que:

En una sucesión aritmética la diferencia entre dos elementos consecutivos es siempre la misma y a esa cantidad se le llama la diferencia de la sucesión aritmética.
En una sucesión geométrica el cociente entre dos elementos consecutivos es siempre el mismo y a esa cantidad se le llama la razón de la sucesión geométrica.'''

a = int(input("Ingrese A: "))
b = int(input("Ingrese B: "))
c = int(input("Ingrese C: "))

if (a-b == b-c):
    print('A,B y C forman una sucesion aritmetica')
elif(a/b == b/c):
    print('A,B y C forman una sucesion geometrica')
else:
    print('A,B y C no forman una sucesion geometrica ni aritmetica')