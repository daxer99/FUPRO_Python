''' A partir de una tupla numérica, devuelva la suma de sus elementos.'''
tupla = (1,1,1,2,3,4)
print(sum(tupla))

suma = 0
for i in range(len(tupla)):
    suma +=tupla[i]

print(suma)