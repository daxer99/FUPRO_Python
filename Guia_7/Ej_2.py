''' Diseñe e implemente una función que reciba como parámetro un número natural e indique: True si es un número primo y False si no lo es.
Compruebe su correcto funcionamiento con dos valores ingresados por el usuario.'''

def es_primo(numero):
    contador = 0
    for n in range(2, numero):
        if numero % n == 0:
            contador = contador + 1
    if contador > 0:
        return False
    else:
        return True

a = 5
b = 15
print(es_primo(a))
print(es_primo(b))