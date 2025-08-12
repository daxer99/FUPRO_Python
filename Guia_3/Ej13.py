n = int(input("¿Cuántos números ingresará? "))
if n == 0:
    print("No se ingresaron números.")
else:
    numeros = []
    for i in range(n):
        num = float(input(f"Ingrese número {i+1}: "))
        numeros.append(num)
    mayor = max(numeros)
    menor = min(numeros)
    media = sum(numeros) / n
    print(f"Mayor: {mayor}, Menor: {menor}, Media: {media:.2f}")