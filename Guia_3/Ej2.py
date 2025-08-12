suma = 0
num = int(input("Ingrese un número (-1 para terminar): "))
while num != -1:
    suma += num
    num = int(input("Ingrese otro número (-1 para terminar): "))
print("La suma es:", suma)