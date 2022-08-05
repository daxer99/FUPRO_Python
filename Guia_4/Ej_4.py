"4. Escribir un programa en Python que pida al usuario una palabra y muestre por pantalla si es un palíndromo."

palabra = input('Ingrese palabra: ')
palabra_invertida = ''

for i in range(len(palabra)-1,-1,-1):
    palabra_invertida = palabra_invertida + palabra[i]
if palabra == palabra_invertida:
    print('Es palíndromo')
else:
    print('No es palíndromo')