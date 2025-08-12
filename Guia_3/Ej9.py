n = int(input("Ingrese un número: "))
suma = 0
while n > 0:
    digito = n % 10
    suma += digito
    n //= 10
print("La suma de los dígitos es:", suma)