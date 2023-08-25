'''Escriba un programa que reciba un numero entero por parte del usuario y devuelva la cantidad de digitos que conforman dicho numero'''
num = int(input("Enter an integer: "))
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits:", count)