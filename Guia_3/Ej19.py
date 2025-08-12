import random as rd

mayor_1 = 0
mayor_2 = 0
menor = 5000
suma = 0

for i in range(10):
    numero = rd.randint(1,5000)
    suma += numero
    # print(numero)

    if numero < menor:
        menor = numero

    if numero > mayor_1:
        aux = mayor_1
        mayor_1 = numero
        mayor_2 = aux
    elif numero > mayor_2:
        mayor_2 = numero

print("Media: ",suma/50)
print("Mayores: ",mayor_1," | ",mayor_2)
print("Menor: ",menor)