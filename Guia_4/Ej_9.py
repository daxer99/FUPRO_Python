'''9. Escriba un programa que pida al usuario que ingrese una frase.Cuente y muestre cuántas palabras contiene la frase.
Considere que las palabras están separadas por espacios simples. No cuente espacios extra (múltiples espacios entre palabras) como palabras.
Restricciones: No usar funciones avanzadas de str.'''

frase = input("Ingrese una frase: ")
palabras = 0
en_palabra = False

for caracter in frase:
    if caracter != ' ':
        if not en_palabra:
            palabras += 1
            en_palabra = True
    else:
        en_palabra = False

print(f"Número de palabras: {palabras}")