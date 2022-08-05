nombres = []

nombre = input("Ingrese nombre, fin para terminar: ")

while nombre !="fin":
    nombres.append(nombre)
    nombre = input("Ingrese nombre, fin para terminar: ")

nombres_ordenados = sorted(nombres)

for i in nombres_ordenados:
    print(i)