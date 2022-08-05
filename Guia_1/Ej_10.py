"""
Un usuario desea conocer cuánto le cuesta el combustible de cada viaje que realiza en su auto.
Para ello anota el kilometraje que marca el odómetro justo antes de iniciar el viaje,
y toma nota nuevamente justo al llegar a destino. Conoce además el consumo de nafta del vehículo en ruta
(es decir, cuantos litros gasta en promedio por cada kilómetro recorrido), y el precio del litro de nafta.
Escriba un algoritmo para calcular el costo de un viaje.
¿Cómo modificaría el algoritmo para considerar un % de descuento para los días en que hay promociones para clientes habituales en la estación de servicio?
"""

inicio_viaje = float(input('Ingrese kilometros antes del viaje: '))
fin_viaje = float(input('Ingrese kilometros despues del viaje: '))

consumo_combustible = 0.09 # cantidad de litros consumidos / kmts recorridos, ver manual del vehículo, varía segun se transite en ruta o ciudad
precio_litro_nafta = 125 #en caso de ser dia de descuento, se multiplica el precio por el porcentaje de descuento

distancia_recorrida = fin_viaje - inicio_viaje
litros_consumidos = distancia_recorrida * consumo_combustible
costo_viaje = litros_consumidos * precio_litro_nafta
costo_viaje = round(costo_viaje,2)

print('El costo del viaje es: $',costo_viaje)