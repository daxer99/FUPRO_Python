# ------------------------------------------------------------------
# Ejercicio 14: Cadena complementaria y complementaria inversa de ADN
# ------------------------------------------------------------------
print("\nEjercicio 14: Complementaria de ADN")
 
secuencia = "ATGCAAATTGTGTGTGCATAATTTATATAGGCTAGAATAGAATCGCTA"
print("Secuencia original:      ", secuencia)
 
# Construimos la cadena complementaria base por base
complementaria = ""
for base in secuencia:
    if base == "A":
        complementaria += "T"
    elif base == "T":
        complementaria += "A"
    elif base == "C":
        complementaria += "G"
    elif base == "G":
        complementaria += "C"
    else:
        complementaria += base  # por si aparece un caracter inesperado
 
print("Cadena complementaria:   ", complementaria)
 
# La complementaria inversa es la complementaria leída de derecha a izquierda
complementaria_inversa = ""
indice = len(complementaria) - 1
while indice >= 0:
    complementaria_inversa += complementaria[indice]
    indice -= 1
 
print("Complementaria inversa:  ", complementaria_inversa)
