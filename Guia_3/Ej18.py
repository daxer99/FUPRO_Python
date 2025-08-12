import random as r
pago_normal = 20
pago_extra = 30
for i in range(1, 11):
    horas = r.randint(36,52)
    if horas <= 40:
        salario = horas * pago_normal
    else:
        salario = 40 * pago_normal + (horas - 40) * pago_extra
    print(f"Empleado {i}: ${salario}")