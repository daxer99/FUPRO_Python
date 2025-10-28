import csv

def cargar_datos(nombre_archivo):
    """Carga los datos del archivo CSV y los retorna como lista de diccionarios"""
    datos = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                fila['asistencia'] = int(fila['asistencia'])
                datos.append(fila)
        return datos
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
        return []


def extraer_mes(fecha_str):
    """Extrae el mes de una fecha en formato dd/mm/aa"""
    partes = fecha_str.split('/')
    return int(partes[1])  # Retorna el mes como entero


def extraer_dia(fecha_str):
    """Extrae el día de una fecha en formato dd/mm/aa"""
    partes = fecha_str.split('/')
    return int(partes[0])  # Retorna el día como entero


def es_otono(mes, dia):
    """Determina si una fecha está en otoño 2024 (20 marzo - 20 junio)"""
    if mes == 3 and dia >= 20:
        return True
    elif 4 <= mes <= 5:
        return True
    elif mes == 6 and dia <= 20:
        return True
    return False


def cantidad_generos_diferentes(datos):
    """A) Retorna la cantidad de géneros diferentes"""
    generos = set()
    for pelicula in datos:
        generos.add(pelicula['género'])
    return len(generos)


def peliculas_accion_julio(datos):
    """B) Retorna cantidad de películas de Acción en julio 2024"""
    contador = 0
    for pelicula in datos:
        mes = extraer_mes(pelicula['Fecha'])
        if pelicula['género'] == 'Acción' and mes == 7:
            contador += 1
    return contador


def peliculas_sala_3d_otono(datos):
    """C) Retorna cantidad de películas en sala 3D durante otoño 2024"""
    contador = 0
    for pelicula in datos:
        if pelicula['sala'] == '3D':
            fecha = pelicula['Fecha']
            mes = extraer_mes(fecha)
            dia = extraer_dia(fecha)
            if es_otono(mes, dia):
                contador += 1
    return contador


def porcentaje_asistencia_mayor_50(datos):
    """D) Retorna porcentaje de películas con asistencia > 50"""
    total_peliculas = len(datos)
    if total_peliculas == 0:
        return 0

    contador_mayor_50 = 0
    for pelicula in datos:
        if pelicula['asistencia'] > 50:
            contador_mayor_50 += 1

    return (contador_mayor_50 / total_peliculas) * 100


def main():
    # Cargar datos
    datos = cargar_datos("peliculas_2024.csv")

    if not datos:
        print("No se pudieron cargar los datos.")
        return

    print("=== ANÁLISIS DE PELÍCULAS 2024 ===\n")

    # A) Cantidad de géneros diferentes
    generos_diferentes = cantidad_generos_diferentes(datos)
    print(f"A) Cantidad de géneros diferentes: {generos_diferentes}")

    # B) Películas de Acción en julio
    accion_julio = peliculas_accion_julio(datos)
    print(f"B) Películas de Acción en julio 2024: {accion_julio}")

    # C) Películas en sala 3D durante otoño
    sala_3d_otono = peliculas_sala_3d_otono(datos)
    print(f"C) Películas en sala 3D durante otoño 2024: {sala_3d_otono}")

    # D) Porcentaje con asistencia > 50
    porcentaje = porcentaje_asistencia_mayor_50(datos)
    print(f"D) Porcentaje con asistencia > 50: {porcentaje:.2f}%")

    # Información adicional
    print(f"\n--- Información adicional ---")
    print(f"Total de registros procesados: {len(datos)}")

    # Mostrar géneros disponibles
    generos = set(pelicula['género'] for pelicula in datos)
    print(f"Géneros encontrados: {', '.join(sorted(generos))}")


if __name__ == "__main__":
    main()