"""
Escribir un programa en Python para una empresa que tiene salas de juegos para todas las edades y quiere calcular de
forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad
y mostrar el precio de la entrada.
Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $150 y si es mayor de 18 años, $250.
"""

edad = int(input('Ingrese edad: '))

if edad < 4:
    print('Costo de entrada: gratis')
elif 4 <= edad < 18:
    print('Costo de entrada: $150')
else:
    print('Costo de entrada: $250')