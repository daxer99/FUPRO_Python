'''Escriba un programa que devuelva el reverso de un numero entero ingresado por el usuario'''

n = int(input("Ingrese numero: "))
reversed_num = 0
while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n //= 10
print(reversed_num)
