"""
Escriba un programa en Python donde se Ingresen tres números e informe el mayor.
"""

a = int(input('Ingrese primer número: '))
b = int(input('Ingrese segundo número: '))
c = int(input('Ingrese tercer número: '))

if a<b:
    if a<c:
        if b<c:
            print(a, b, c)
        else:
            print(a, c, b)
    else:
        print(c, a, b)
elif b<c:
    if a<c:
        print(b, a, c)
    else:
        print(b, c, a)
else:
    print(c, b, a)