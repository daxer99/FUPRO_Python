'''Genere una secuencia de 1000 números aleatorios entre 0 y 1, con dos decimales.
Obtenga un listado donde se registre la cantidad de veces que aparece cada uno de los valores,
como pares: (valor, cant.).'''
import random

test_tuple = tuple(round(random.random(),2) for i in range(1000))

x=list(test_tuple)
y=[]
res = []
for i in x:
    if i not in y:
        y.append(i)
for i in range(len(y)):
    res.append((y[i],x.count(y[i])))

print(res)