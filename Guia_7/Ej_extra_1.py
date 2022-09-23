'''calcular IMC'''

def calcular_IMC(peso,altura):
    return round(peso/altura**2,2)

peso = 90
altura = 1.75

print("IMC: ",calcular_IMC(peso,altura))