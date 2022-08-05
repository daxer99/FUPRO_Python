'''3. Escriba un programa que pregunte cuántos números se van a introducir, pida esos números e informe el mayor, el menor y la media.
'''

n = int(input("¿cuantos numeros se van a ingresar?\n"))
mayor = 0
menor = 1000000000
suma = 0

for i in range(n):
    numero = int(input("Ingrese numero: "))

    suma += numero

    if numero < menor:
        menor = numero

    if numero > mayor:
        mayor = numero

media = suma/n

print("Menor: ",menor)
print("Mayor: ",mayor)
print("Media: ",media)