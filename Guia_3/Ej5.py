positivos = 0
num = int(input("Ingrese un número: "))
while num >= 0:
    positivos += 1
    num = int(input("Ingrese otro número: "))
print(f"Se ingresaron {positivos} números positivos.")