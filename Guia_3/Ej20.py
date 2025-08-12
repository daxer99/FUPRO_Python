import random
contador = 0
for i in range(20):
    num = random.uniform(0, 1)
    print(f"Número {i+1}: {num:.3f}")
    if num > 0.5:
        contador += 1
print(f"{contador} números fueron mayores que 0.5.")