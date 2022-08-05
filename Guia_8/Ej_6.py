def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

# for i in range(10):
#     print(fibonacci(i))

nombre_archivo = input('Indique nombre de archivo: ')
n = int(input('Cantidad de números: '))

# Forma 1
# with open(nombre_archivo,'w') as file:
#     file.write('Serie de Fibonacci para' + str(n) + ' números: \n')
#     for i in range(n):
#         file.write(str(fibonacci(i)))
#         file.write(' ')

# Forma 2
file = open(nombre_archivo, 'w')
file.write('Serie de Fibonacci para ' + str(n) + ' números: \n')
for i in range(n):
    file.write(str(fibonacci(i)))
    file.write(' ')
file.close()