import random
L = []
for i in range(10):
    L.append(random.randint(53,268))

for i in range (16):
    cod_art = random.randint(0,9)
    ventas = random.randint(1,50)
    if ventas > L[cod_art]:
        print('No hay stock suficiente del articulo. Disponible:',L[i])
    else:
        L[cod_art]-=ventas