# ------------------------------------------------------------------
# Ejercicio 16: Invertir una oración palabra por palabra
# ------------------------------------------------------------------
print("\nEjercicio 16: Invertir oración")
 
oracion = input("Ingrese una oración: ")
 
# Recorremos la oración de atrás para adelante, armando cada palabra
# y agregándola al resultado a medida que la completamos.
oracion_invertida = ""
palabra_actual = ""
 
indice = len(oracion) - 1
while indice >= 0:
    caracter = oracion[indice]
    if caracter != " ":
        # Vamos armando la palabra actual (al revés, letra por letra)
        palabra_actual = caracter + palabra_actual
    else:
        # Encontramos un espacio: la palabra armada está completa
        if palabra_actual != "":
            if oracion_invertida == "":
                oracion_invertida = palabra_actual
            else:
                oracion_invertida = oracion_invertida + " " + palabra_actual
            palabra_actual = ""
    indice -= 1
 
# Agregamos la última palabra (la primera de la oración original)
if palabra_actual != "":
    if oracion_invertida == "":
        oracion_invertida = palabra_actual
    else:
        oracion_invertida = oracion_invertida + " " + palabra_actual
 
print("Oración invertida:", oracion_invertida)
