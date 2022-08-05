"1. Lea el archivo personal.txt que contiene un listado con los nombres  y apellidos de los agentes de la Facultad de Ingeniería de la UNER, y muestre el contenido del mismo por consola."

with open('personal.txt', 'r') as file:
    print('Datos del objeto file')
    print(file, '\n')
    print('Contenido del archivo file')
    print(file.read())

# file_r = open('personal.txt','r')

# print('Datos del objeto file_r')
# print(file_r,'\n')

# print('Contenido del archivo file_r')
# print(file_r.read())

# print('')

# print('Contenido de los primeros 7 char del archivo file_r, antes de seek()')
# print(file_r.read(7))
# print('tell:',file_r.tell())
# print('Contenido de los primeros 7 char del archivo file_r, despúes de seek()')
# file_r.seek(0)
# print(file_r.read(7))
# print('tell:',file_r.tell())

# print('')
# print("Cantidad de caracteres por linea")
# file_r.seek(0)
# for linea in file_r:
#     cantidad = len(linea)
#     print(linea, cantidad)

# file_r.close()