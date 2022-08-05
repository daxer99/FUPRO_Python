"2. Escribir un programa en Python en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase."

frase = input('Ingrese frase:\n')
letra = input('Ingrese letra:\n')

cantidad = frase.count(letra)

print('En la frase:', frase, 'hay', cantidad, 'letras', letra)