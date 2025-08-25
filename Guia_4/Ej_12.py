'''Escriba un programa que pida al usuario una frase (por ejemplo, nombre de una organización) y genere un acrónimo usando la primera letra de cada palabra, en mayúsculas.'''
frase = input("Ingrese una frase para generar acrónimo: ")
acrónimo = ""
es_primera_letra = True  # La primera letra de la frase es parte del acrónimo

for caracter in frase:
    if caracter.isalpha():
        if es_primera_letra:
            acrónimo += caracter.upper()
            es_primera_letra = False
    else:
        es_primera_letra = True  # Próximo carácter alfabético será inicio de palabra

print("Acrónimo:", acrónimo)