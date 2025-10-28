import csv
import random
from datetime import datetime, timedelta


def generar_datos_peliculas():
    # Listas de datos para generar registros realistas
    peliculas = [
        "Avatar: El camino del agua", "Misión Imposible 7", "Guardianes de la Galaxia Vol. 3",
        "Fast X", "The Flash", "Indiana Jones 5", "Transformers: El despertar de las bestias",
        "John Wick 4", "Ant-Man y la Avispa: Quantumania", "Oppenheimer",
        "Barbie", "Spider-Man: A través del Spider-Verso", "The Marvels",
        "Dune: Parte dos", "Wonka", "Killers of the Flower Moon", "Napoleon",
        "Aquaman y el reino perdido", "Five Nights at Freddy's", "Meg 2: La fosa",
        "Blue Beetle", "The Creator", "The Nun 2", "Saw X", "Expend4bles",
        "The Equalizer 3", "Gran Turismo", "The Killer", "Poor Things",
        "The Color Purple", "Wish", "Trolls 3", "Migration", "El chico y la garza",
        "Godzilla Minus One", "Past Lives", "Anatomy of a Fall", "The Holdovers"
    ]

    generos = ["Acción", "Comedia", "Drama", "Terror", "Ciencia Ficción",
               "Aventura", "Animación", "Romance", "Suspenso", "Documental"]

    salas = ["2D", "3D", "IMAX", "VIP", "4DX"]

    # Generar datos
    datos = []

    # Fecha inicial (1 de enero de 2024)
    fecha_inicio = datetime(2024, 1, 1)

    for i in range(1000):
        id_funcion = f"F{20240000 + i + 1}"
        pelicula = random.choice(peliculas)

        # Generar fecha aleatoria en 2024
        dias_aleatorios = random.randint(0, 364)
        fecha = fecha_inicio + timedelta(days=dias_aleatorios)
        fecha_str = fecha.strftime("%d/%m/%y")

        # Asignar género basado en la película (simplificado)
        if any(palabra in pelicula.lower() for palabra in
               ['avatar', 'transformers', 'flash', 'ant-man', 'marvel', 'guardianes']):
            genero = "Ciencia Ficción"
        elif any(palabra in pelicula.lower() for palabra in
                 ['john wick', 'misión imposible', 'equalizer', 'expendables']):
            genero = "Acción"
        elif any(palabra in pelicula.lower() for palabra in
                 ['barbie', 'wish', 'trolls', 'willy wonka', 'winnie the pooh']):
            genero = "Animación"
        elif any(palabra in pelicula.lower() for palabra in ['saw', 'nun', 'freddy', 'terror', 'halloween']):
            genero = "Terror"
        elif any(palabra in pelicula.lower() for palabra in ['oppenheimer', 'napoleon', 'flower moon', 'drama']):
            genero = "Drama"
        else:
            genero = random.choice(generos)

        sala = random.choice(salas)

        # Asistencia más realista (dependiendo de sala y día de la semana)
        if sala == "3D" or sala == "IMAX" or sala == "4DX":
            asistencia_base = random.randint(40, 120)
        else:
            asistencia_base = random.randint(20, 80)

        # Ajustar por día de la semana (fin de semana más concurrido)
        dia_semana = fecha.weekday()
        if dia_semana >= 5:  # Fin de semana
            asistencia = asistencia_base + random.randint(10, 30)
        else:
            asistencia = max(5, asistencia_base - random.randint(0, 20))

        datos.append([id_funcion, pelicula, fecha_str, genero, sala, asistencia])

    return datos


def guardar_csv(datos, nombre_archivo="peliculas_2024.csv"):
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        # Escribir encabezado
        writer.writerow(["ID_funcion", "película", "Fecha", "género", "sala", "asistencia"])
        # Escribir datos
        writer.writerows(datos)

    print(f"Archivo '{nombre_archivo}' generado exitosamente con {len(datos)} registros.")


# Generar y guardar los datos
if __name__ == "__main__":
    datos_peliculas = generar_datos_peliculas()
    guardar_csv(datos_peliculas)