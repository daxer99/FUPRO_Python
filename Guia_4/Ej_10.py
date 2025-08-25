'''10. Escriba un programa que oculte vocales.Pida al usuario una cadena de texto, reemplace cada vocal (a, e, i, o, u, mayúsculas o minúsculas) por el símbolo * y muestre la cadena resultante.
'''

frase = input("Ingrese una frase: ")
resultado = ""

vocales = "aeiouAEIOU"

for caracter in frase:
    if caracter in vocales:
        resultado += "*"
    else:
        resultado += caracter

print("Frase con vocales ocultas:", resultado)