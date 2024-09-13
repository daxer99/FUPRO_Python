juan = 0
maria =0
nombre = input("Ingrese nombre, fin para terminar: ")
while nombre !="fin":
    if nombre.lower() == 'maria':
        maria += 1
    elif nombre.lower() == 'juan':
        juan += 1
    nombre = input("Ingrese nombre, fin para terminar: ")

print("Cantidad de juan:",juan)
print("Cantidad de maria:",maria)