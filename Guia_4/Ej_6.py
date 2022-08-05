"6. Dada una secuencia de ADN, escriba un programa para calcular el porcentaje de GC, es decir la cantidad porcentual de guaninas (G) y citosinas (C) que posee la secuencia."

secuencia_adn = 'ATGCAAATTGTGTGTGCATAATTTATATAGGCTAGAATAGAATCGCTA'
cantidad_G = secuencia_adn.count('G')
cantidad_C = secuencia_adn.count('C')
cantidad_GC = cantidad_G + cantidad_C
porcentaje_GC = (cantidad_GC / len(secuencia_adn))*100

print('El porcentaje de GC es:', porcentaje_GC,'%')