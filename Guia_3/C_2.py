'''Escriba un programa que sume los digitos de un numero entero ingresado por el usuario'''

num = int(input("Enter an integer: "))
sum_of_digits = 0

while num != 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10

print("Sum of digits:", sum_of_digits)