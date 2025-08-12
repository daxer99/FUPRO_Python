mayor = None
num = int(input("Ingrese un número (0 para terminar): "))
while num != 0:
    if mayor is None or num > mayor:
        mayor = num
    num = int(input("Ingrese otro número (0 para terminar): "))
if mayor is not None:
    print(f"El mayor número fue: {mayor}")
else:
    print("No se ingresaron números.")