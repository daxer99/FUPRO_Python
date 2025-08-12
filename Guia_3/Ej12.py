n = int(input("¿Cuántos números desea sumar? "))
suma = 0
for i in range(n):
    num = int(input(f"Ingrese número {i+1}: "))
    suma += num
print("La suma es:", suma)