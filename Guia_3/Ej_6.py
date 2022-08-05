'''6. Escriba un programa en Python que informe los números primos menores que 100.'''

contador = 0
numero = 2

while numero < 100:
    for n in range(2, numero):
        if numero % n == 0:
            contador = contador + 1

    if contador == 0:
        print(numero)

    contador = 0
    numero = numero + 1