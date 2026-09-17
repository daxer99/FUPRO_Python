# ------------------------------------------------------------------
# Ejercicio 15: Validación simple de contraseña
# ------------------------------------------------------------------
print("\nEjercicio 15: Validación de contraseña")
 
contrasena = input("Ingrese una contraseña: ")
 
tiene_longitud_minima = len(contrasena) >= 8
tiene_mayuscula = False
tiene_minuscula = False
tiene_numero = False
 
for caracter in contrasena:
    if caracter.isupper():
        tiene_mayuscula = True
    elif caracter.islower():
        tiene_minuscula = True
    elif caracter.isdigit():
        tiene_numero = True
 
if tiene_longitud_minima and tiene_mayuscula and tiene_minuscula and tiene_numero:
    print("La contraseña es VÁLIDA.")
else:
    print("La contraseña NO es válida. No cumple con:")
    if not tiene_longitud_minima:
        print("- Longitud mínima de 8 caracteres")
    if not tiene_mayuscula:
        print("- Al menos una letra mayúscula")
    if not tiene_minuscula:
        print("- Al menos una letra minúscula")
    if not tiene_numero:
        print("- Al menos un número")
