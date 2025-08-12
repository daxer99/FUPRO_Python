numero = int(input("Ingrese número: "))
contador = 0

for n in range(2, numero):
    if numero % n == 0:
        contador = contador + 1

if contador > 0:
    print(numero, 'no es primo')
else:
    print(numero, 'es primo')