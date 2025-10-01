'''Una asociación cooperadora escolar recibe aportes de dinero variable de los estudiantes asociados. Se leen sin orden alguno los montos aportados en el último año y la fecha correspondiente (día, mes). Estos datos terminan con el valor de monto cero. Informe:
a. el total recaudado por mes.
b. El mes de menor aporte.
Para resolver el problema organice los datos en una lista de 12 elementos.'''

aportes = []
for i in range(12):
    aportes.append(0)

aportes = [0 for i in range(12) if True]

dia = input("Ingrese dia: ")
mes = int(input("Ingrese mes: "))
monto = float(input("Ingrese monto: "))

while monto !=0:
    aportes[mes-1] += monto

    dia = input("Ingrese dia: ")
    mes = int(input("Ingrese mes: "))
    monto = float(input("Ingrese monto"))

for i in range(len(aportes)):
    print("La recaudacion del mes "+str(i+1)+ " fue de: ",aportes[i])

menor_recaudacion = aportes[0]
mes_menor_recaudacion = 0
for i in range(len(aportes)):
    if aportes[i]<menor_recaudacion:
        mes_menor_recaudacion = i

# menor_recaudacion = min(aportes)
# mes_menor_recaudacion = aportes.index(menor_recaudacion)
print("El mes de menor recaudacion es: ",mes_menor_recaudacion+1)