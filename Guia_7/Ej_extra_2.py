'''hacer generala (en cuantos tiros)'''
import random

def dado():
    return random.randint(1,6)

seguir = True
contador = 0
while seguir:
    contador +=1
    a = dado()
    if a == dado() == dado() == dado() == dado():
        seguir = False

print("En ",contador, " tiros se obtuvo generala del numero ",a)