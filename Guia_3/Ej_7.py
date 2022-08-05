''' Escriba un programa en Python que informe los primeros 100 números primo.'''

cant_nros_primos = 10
contador = 0
numero = 2
i = 0

while i < cant_nros_primos:
    for n in range(2, numero):
        if numero % n == 0:
            contador = contador + 1

    if contador == 0:
        print(numero)
        i = i + 1

    contador = 0
    numero = numero + 1