'''En una secuencia de ADN se define una isla CpG como una secuencia de 4 o más nucleótidos de C y/o G seguidos.
Implemente una función que reciba una secuencia de ADN como un string  y determine la cantidad, tamaño y posición de las islas CpG presentes en esa cadena.
Lea el archivo FragmentoCromo1.txt que contiene un nucleótido por línea y llame a la función implementada.'''

def encontrar_islas_cpg(secuencia):
    """
    Encuentra todas las islas CpG en una secuencia de ADN.
    Una isla CpG es una subsecuencia de al menos 4 nucleótidos consecutivos
    compuestos únicamente por 'C' y/o 'G'.

    Parámetros:
        secuencia (str): Cadena de ADN (ej. "ATCGGCCGTA...")

    Retorna:
        list: Lista de diccionarios con claves 'inicio', 'tamaño'
    """
    islas = []
    i = 0
    n = len(secuencia)

    while i < n:
        if secuencia[i] in 'CG':
            # Inicia una posible isla
            inicio = i
            while i < n and secuencia[i] in 'CG':
                i += 1
            tamaño = i - inicio
            if tamaño >= 4:
                islas.append({'inicio': inicio, 'tamaño': tamaño})
        else:
            i += 1

    return islas


def leer_secuencia_desde_archivo(ruta_archivo):
    """
    Lee un archivo con un nucleótido por línea y devuelve una cadena.
    """
    with open(ruta_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    # Eliminar saltos de línea y espacios, y unir
    secuencia = ''.join(linea.strip() for linea in lineas)
    return secuencia

ruta = 'FragmentoCromo1.txt'
try:
    secuencia = leer_secuencia_desde_archivo(ruta)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{ruta}'.")

islas = encontrar_islas_cpg(secuencia)

print(f"Total de islas CpG encontradas: {len(islas)}\n")
if islas:
   for idx, isla in enumerate(islas, 1):
        print(f"Isla {idx}:")
        print(f"  - Posición de inicio: {isla['inicio']}")
        print(f"  - Tamaño: {isla['tamaño']}")
        # Opcional: mostrar la subsecuencia real
        subseq = secuencia[isla['inicio']:isla['inicio'] + isla['tamaño']]
        print(f"  - Secuencia: {subseq}")
        print()
else:
    print("No se encontraron islas CpG.")
