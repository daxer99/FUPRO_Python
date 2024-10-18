'''9. Una empresa distribuidora de equipos médicos vende 10 artículos distintos y exporta a otros países. Posee 8 sucursales y desea analizar el desempeño de las mismas en el 2020. Para ello se ingresan 4 datos por cada operación de venta realizada en  ese año: mes (1..12), sucursal(1..8), moneda (‘U’ o ‘P’), monto. El dato moneda indica si el monto de la operación es en dólares (‘U’) o en pesos (‘P’).  Puede haber varias ventas en un mismo mes y para una misma sucursal.
a) Organice la información ingresada acumulando por separado los montos vendidos en pesos y en dólares.
b) Determine la recaudación anual en USD  y en pesos de la sucursal 7.
c) En el mes de mayo, cuál fue la mayor recaudación en dólares de una sucursal? Y qué sucursal lo logró?
Use funciones para los puntos b y c.'''

def recaudacion_sucursal(datos,sucursal):
    return sum(datos[sucursal-1])

def sucursal_mayor_recaudacion_por_mes(datos,mes):
    mayor = 0
    suc_mayor = 0
    for i in range(8):
        if sum(datos[i][mes-1]) > mayor:
            mayor = sum(datos[i][mes-1])
            suc_mayor = i + 1
    return mayor,suc_mayor

usd = [[0]*12 for i in range(8)]
pesos = [[0]*12 for i in range(8)]

mes = int(input('Ingrese mes, 0 para terminar: '))
while mes !=0:
    suc = int(input("Ingrese sucursal: "))
    moneda = input("Ingrese moneda: U o P: ")
    monto = float(input("Ingrese monto: "))
    if moneda.upper() == 'P':
        pesos[suc-1][mes-1] += monto
    if moneda.upper() == 'U':
        usd[suc-1][mes-1] += monto
    mes = int(input('Ingrese mes, 0 para terminar: '))

#B
print("Recaudacion anual sucursal 7 en dolares:",recaudacion_sucursal(usd,7))
print("Recaudacion anual sucursal 7 en pesos:",recaudacion_sucursal(pesos,7))
#C
mayor_recaudacion_mayo,sucursal_mayor_recaudacion_mayo = sucursal_mayor_recaudacion_por_mes(usd,5)
print("En mayo la mayor recaudacion fue de",mayor_recaudacion_mayo,"por la sucursal",sucursal_mayor_recaudacion_mayo)