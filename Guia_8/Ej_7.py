def calcularIMC(peso, altura):
    imc = peso / altura ** 2
    return round(imc, 2)


def definirEstadoIMC(imc):
    estadoIMC = ''
    if imc <= 18.5:
        estadoIMC = 'infrapeso'
    elif 1.85 < imc <= 25:
        estadoIMC = 'normal'
    elif 25 < imc <= 30:
        estadoIMC = 'Sobrepeso'
    else:
        estadoIMC = 'Obesidad'
    return estadoIMC

nom = "Rodrigo"
ape = "Peralta"
edad = "28"
dni = "37562461"
peso = 85.5
altura = 1.75

with open("datos_imc.txt", "w") as file:
    file.write("Nombre: " + nom)
    file.write('\n')
    file.write("Apellido: " + ape)
    file.write('\n')
    file.write("Edad: " + edad)
    file.write('\n')
    file.write("DNI: " + dni)
    file.write('\n')
    file.write("IMC: " + str(calcularIMC(peso, altura)) + " kg/m²")
    file.write('\n')
    file.write("Condición: " + definirEstadoIMC(calcularIMC(peso, altura)))
    file.write('\n')