'''6. Se ingresan por pantalla las coordenadas x, y, z del recorrido de un alpinista tomadas cada 15 segundos mientras escala una montaña.
El ingreso de datos finaliza con la terna [0, 0, 0]. Almacene los datos en una lista y determine:
a) La cantidad de veces que el alpinista debió descender para sortear algún obstáculo.
b) La amplitud del desplazamiento en x (Max “x” – Min “x”).
c) El tiempo total empleado en el ascenso.
d) El tiempo de descanso del alpinista.'''

#A
coordenadas = []

while True:
    x = int(input('Ingrese coordenada X: '))
    y = int(input('Ingrese coordenada Y: '))
    z = int(input('Ingrese coordenada Z: '))
    if [x,y,z] == [0,0,0]:
        break
    else:
        coordenadas.append([x,y,z])

#A
cant_descensos = 0
for i in range(1,len(coordenadas)):
    if coordenadas[i-1][2] > coordenadas[i][2]:
        cant_descensos += 1
print(cant_descensos,'el alpinista descendio para sortear algun obstaculo')

#B
max_x = 0
min_x = 1000000
for i in range(len(coordenadas)):
    if coordenadas[i][0] > max_x:
        max_x = coordenadas[i][0]
    if coordenadas[i][0] < min_x:
        min_x = coordenadas[i][0]
desplazamiento = max_x - min_x
print('El desplazamiento en X fue de:',desplazamiento)

#C
tiempo_total = len(coordenadas)*15
print('El tiempo total fue de:',tiempo_total,'segundos')

#D
descanso = 0
for i in range(1,len(coordenadas)):
    if coordenadas[i-1] == coordenadas[i]:
        descanso += 1
print(descanso*15,'segundos el alpinista descanso en el trayecto')