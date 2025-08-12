n = int(input("Ingrese un número: "))
print("Números impares:")
for i in range(1, n + 1):
    if i % 2 == 1:
        print(i)