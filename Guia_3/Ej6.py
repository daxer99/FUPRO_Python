saldo = 1000
while True:
    retiro = float(input("¿Cuánto desea retirar? (0 para salir): "))
    if retiro == 0:
        break
    if retiro > saldo:
        print("Saldo insuficiente. El programa ha terminado.")
        break
    saldo -= retiro
    print(f"Retiro exitoso. Saldo restante: {saldo}")