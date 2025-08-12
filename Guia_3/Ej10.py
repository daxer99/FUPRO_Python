import random
lanzamientos = 0
dado = 0
while dado != 6:
    dado = random.randint(1, 6)
    lanzamientos += 1
    print(f"Lanzamiento {lanzamientos}: {dado}")
print(f"Se obtuvo un 6 después de {lanzamientos} lanzamientos.")