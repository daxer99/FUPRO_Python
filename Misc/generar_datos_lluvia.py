import random


def generar_datos_lluvias():
    """Genera datos de lluvias para 10 localidades durante enero"""

    localidades = [
        "Localidad Norte", "Localidad Sur", "Localidad Este", "Localidad Oeste",
        "Localidad Centro", "Valle Verde", "Costa Azul", "Sierra Alta",
        "Llanura Central", "Bosque Verde"
    ]

    datos = []

    # Generar datos para cada día de enero (31 días)
    for dia in range(1, 32):
        for localidad_id in range(1, 11):
            # Múltiples registros por localidad y día (entre 1 y 3 estaciones)
            num_registros = random.randint(1, 3)

            for registro in range(num_registros):
                # Generar lluvia más realista (algunos días sin lluvia, otros con mucha)
                if random.random() < 0.3:  # 30% de probabilidad de día sin lluvia
                    mm_lluvia = 0
                else:
                    # Lluvia variable según la localidad
                    base_lluvia = random.randint(1, 50)
                    # Algunas localidades más lluviosas que otras
                    if localidad_id in [2, 7]:  # Localidad Sur y Costa Azul más lluviosas
                        mm_lluvia = base_lluvia + random.randint(10, 40)
                    elif localidad_id in [5, 9]:  # Localidad Centro y Bosque Verde medianas
                        mm_lluvia = base_lluvia + random.randint(5, 20)
                    else:
                        mm_lluvia = base_lluvia

                fecha = f"{dia:02d}/01/2024"
                datos.append(f"{localidad_id}-{fecha}-{mm_lluvia}")

    return datos


def guardar_archivo_lluvias(datos, nombre_archivo="lluvias_enero.txt"):
    """Guarda los datos en un archivo de texto"""
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        for linea in datos:
            archivo.write(linea + '\n')

    print(f"Archivo '{nombre_archivo}' generado exitosamente con {len(datos)} registros.")


# Generar y guardar los datos
if __name__ == "__main__":
    datos_lluvias = generar_datos_lluvias()
    guardar_archivo_lluvias(datos_lluvias)