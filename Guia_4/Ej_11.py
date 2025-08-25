'''En criptografía, el cifrado César es una de las técnicas más simples y más usadas. Es un tipo de cifrado por sustitución en el que una letra en el texto original es reemplazada por otra letra que se encuentra un número fijo de posiciones más adelante en el alfabeto. Por ejemplo, con un desplazamiento de 3, la A sería sustituida por la D (situada 3 lugares a la derecha de la A). Este méttodo debe su nombre a Julio César, que lo usaba para comunicarse con sus generales.
Escriba un programa en Python que implemente un cifrado César simpl.Pida al usuario una cadena de texto (solo letras, sin tildes),pida un número entero (desplazamiento, por ejemplo: 3),mueva cada letra del alfabeto n posiciones hacia adelante (circular: después de 'z' viene 'a'), solo aplique el cifrado a letras; ignore espacios y otros caracteres, muestre el texto cifrado.'''
texto = input("Ingrese el texto a cifrar (solo letras): ")
desplazamiento = int(input("Ingrese el desplazamiento: "))
cifrado = ""

for caracter in texto:
    if 'a' <= caracter <= 'z':
        codigo = ord(caracter) - ord('a')
        nuevo_codigo = (codigo + desplazamiento) % 26
        nuevo_caracter = chr(nuevo_codigo + ord('a'))
        cifrado += nuevo_caracter
    elif 'A' <= caracter <= 'Z':
        codigo = ord(caracter) - ord('A')
        nuevo_codigo = (codigo + desplazamiento) % 26
        nuevo_caracter = chr(nuevo_codigo + ord('A'))
        cifrado += nuevo_caracter
    else:
        cifrado += caracter  # Mantener espacios, signos, etc.

print("Texto cifrado:", cifrado)