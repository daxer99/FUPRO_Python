# ------------------------------------------------------------------
# Ejercicio 13: Anagramas
# ------------------------------------------------------------------
print("Ejercicio 13: Anagramas")
 
cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")
 
# Normalizamos: pasamos a minúsculas y quitamos espacios (sin usar listas)
cadena1_normalizada = ""
for caracter in cadena1.lower():
    if caracter != " ":
        cadena1_normalizada += caracter
 
cadena2_normalizada = ""
for caracter in cadena2.lower():
    if caracter != " ":
        cadena2_normalizada += caracter
 
es_anagrama = True
 
# Si tienen distinta longitud, no pueden ser anagramas
if len(cadena1_normalizada) != len(cadena2_normalizada):
    es_anagrama = False
else:
    # Para cada caracter de la primera cadena, contamos cuántas veces
    # aparece en cada cadena y comparamos esos conteos
    for caracter in cadena1_normalizada:
        if cadena1_normalizada.count(caracter) != cadena2_normalizada.count(caracter):
            es_anagrama = False
 
if es_anagrama:
    print(f'"{cadena1}" y "{cadena2}" SON anagramas.')
else:
    print(f'"{cadena1}" y "{cadena2}" NO son anagramas.')
