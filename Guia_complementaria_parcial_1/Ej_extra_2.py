'''encuentre el mayor de una lista y muestre el anterior y el siguiente'''
import random

lista = [random.randint(0,10) for i in range(25)]
mayor = max(lista)

print(lista)
for i in range(25):
    if lista[i] == mayor:
        print(lista[i-1],lista[i+1])