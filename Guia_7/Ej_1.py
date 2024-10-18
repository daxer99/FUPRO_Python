'''1. Diseñe e implemente una función que reciba como parámetro un número natural e indique todos sus divisores.'''

def divisores(numero):
    d = []
    for i in range(1,numero+1):
        if numero%i==0:
            d.append(i)
    return d

N = int(input("Ingrese numero: "))
print("DIvisores:")
print(divisores(N))