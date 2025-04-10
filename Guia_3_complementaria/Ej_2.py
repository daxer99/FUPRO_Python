'''2. Escriba un programa que solicite al usuario ingresar una contraseña numérica.
La contraseña se encuentra almacenada en el programa. El usuario tiene hasta tres intentos para ingresarla en forma correcta.
Ante cada intento se mostrará un mensaje de error o de éxito. Si se superan los tres intentos se mostrará otro mensaje de error y se terminará el programa.'''

pwd = 123
intentos = 0
while intentos < 3:
    contrasena = int(input('Ingrese contraseña: '))
    if contrasena == pwd:
        print("Contraseña correcta")
        break
    intentos = intentos +1
    if intentos == 3:
        print("Cantidad de intentos alcanzada. Fin")
