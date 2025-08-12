'''Dado tres números que representan las longitudes de los lados de un triángulo, escriba un programa que determine si el triángulo es:
Equilátero (todos los lados iguales)
Isósceles (dos lados iguales)
Escaleno (todos los lados diferentes)
Además, verifique si los valores ingresados pueden formar un triángulo (la suma de dos lados debe ser mayor que el tercero).'''

# Pedimos los tres lados del triángulo
lado1 = float(input("Ingrese el primer lado del triángulo: "))
lado2 = float(input("Ingrese el segundo lado del triángulo: "))
lado3 = float(input("Ingrese el tercer lado del triángulo: "))

# Verificamos si los valores pueden formar un triángulo
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    # Clasificación según los lados
    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")
else:
    print("Los valores ingresados no pueden formar un triángulo.")