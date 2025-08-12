'''Una tienda aplica descuentos según la cantidad de productos iguales comprados:
Menos de 10 productos: sin descuento
De 10 a 19 productos: 5% de descuento
20 o más productos: 10% de descuento
Escriba un programa que pida la cantidad de productos del mismo tipo y el precio unitario, y calcule el total a pagar con descuento aplicado (si corresponde).'''

cantidad = int(input("Ingrese cantidad de productos: "))
precio = float(input('Ingrese precio unitario: '))
if cantidad < 10:
    print('total a pagar:',cantidad*precio)
elif 10<= cantidad <20:
    print('total a pagar:',cantidad*precio - cantidad*precio*0.05)
else:
    print('total a pagar:',cantidad*precio - cantidad*precio*0.1)