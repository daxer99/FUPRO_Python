"""
Diseñe e implemente un programa en Python para la creación de direcciones de e-mail institucionales. El usuario debe ingresar su nombre, apellido y el nombre de la empresa o institución a la que pertenece. Las direcciones de e-mail institucionales constan de: la primer letra del nombre del usuario, seguido de su apellido completo, seguido del @, seguido del nombre de la institución y por último un .com. Toda la dirección de e-mail debe estar en minúscula.
Ejemplo: Nombre: Rodrigo
	   Apellido: Peralta
	   Institución: FIUNER
	   Dirección de e-mail institucional: rperalta@fiuner.com
"""

nombre = input('Ingrese nombre: ')
apellido = input('Ingrese apellido: ')
institucion = input('Ingrese institucion: ')

primera_letra_nombre = str.lower(nombre[0])
apellido = str.lower(apellido)
institucion = str.lower(institucion)
email = primera_letra_nombre + apellido + '@' + institucion + '.com'

print('Su dirección de e-mail institucional es:', email)