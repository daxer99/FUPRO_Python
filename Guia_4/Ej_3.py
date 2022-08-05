'''3. Escriba un programa que permita al usuario leer una cadena de caracteres y exhiba un menú con las opciones:
Pasar a Mayúsculas
Pasar a Minúsculas
Solo la inicial con mayúsculas.'''

cadena = input("Ingrese texto: ")
print('''1. Pasar a Mayúsculas
2. Pasar a Minúsculas
3. Solo la inicial con mayúsculas.''')
opcion = int(input("Ingrese opcion: "))
if opcion == 1:
    print(cadena.upper())
elif opcion == 2:
    print(cadena.lower())
elif opcion == 3:
    print(cadena.capitalize())
else:
    print("Opcion incorrecta ingresada")


# Version 2
# cadena = input("Ingrese cadena: ")
# print("")
# opcion = int(input("Ingrese 1: Pasar a Mayúsculas, 2: Pasar a Minúsculas, 3: Solo la inicial con mayúsculas. 0: Salir: "))
# while opcion !=0:
#     if opcion == 1:
#         print(cadena.upper())
#     elif opcion == 2:
#         print(cadena.lower())
#     elif opcion == 3:
#         print(cadena.capitalize())
#     else:
#         print("Opcion incorrecta!!!")
#     print("")
#     opcion = int(input("Ingrese 1: Pasar a Mayúsculas, 2: Pasar a Minúsculas, 3: Solo la inicial con mayúsculas. 0: Salir: "))