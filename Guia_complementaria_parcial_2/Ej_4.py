'''En una secuencia de ADN se define una isla CpG como una secuencia de 4 o más nucleótidos de C y/o G seguidos.
Implemente una función que reciba una secuencia de ADN como un string  y determine la cantidad, tamaño y posición de las islas CpG presentes en esa cadena.
Lea el archivo FragmentoCromo1.txt que contiene un nucleótido por línea y llame a la función implementada.'''

def islas_CpG(secuencia):
    cantidad = 0
    posicion = 0
    posiciones = []
    for i in range(4,len(secuencia)):
        if secuencia[i-4]+secuencia[i-3]+secuencia[i-2]+secuencia[i-1] =="CGCG":
            cantidad +=1
            posicion = i-3
            posiciones.append(posicion)
    return cantidad, posiciones


file = open("/media/rodrigo/Data/Facultad/UNER/FUPRO/Guia_complementaria_parcial_2/FragmentoCromo1.txt")
file = file.readlines()
cromo = ''
for fila in file:
    cromo+=fila.strip("\n")

cantidad,posiciones=islas_CpG(cromo)

print("El archivo contiene ",cantidad," islas CpG en las posiciones: ")
for i in posiciones:
    print(i)