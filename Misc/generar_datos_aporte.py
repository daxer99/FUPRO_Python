import random


def generar_datos_aportes():
    """Genera datos de aportes voluntarios para alumnos"""

    datos = []

    # Generar entre 800 y 1200 aportes
    num_aportes = random.randint(800, 1200)

    for i in range(num_aportes):
        # DNI aleatorio (sin repetir necesariamente)
        dni = random.randint(30000000, 50000000)

        # Curso entre 1 y 5
        curso = random.randint(1, 5)

        # Mes entre 1 y 12
        mes = random.randint(1, 12)

        # Monto aportado (más realista - algunos aportan poco, otros más)
        if random.random() < 0.6:  # 60% aporta montos bajos
            monto = random.randint(100, 500)
        elif random.random() < 0.3:  # 30% aporta montos medios
            monto = random.randint(500, 1000)
        else:  # 10% aporta montos altos
            monto = random.randint(1000, 3000)

        # Formato: DNI, Curso, Mes, Monto
        datos.append(f"{dni},{curso},{mes},{monto}")

    return datos


def guardar_archivo_aportes(datos, nombre_archivo="APORTES.txt"):
    """Guarda los datos en el archivo APORTES.txt"""
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        for linea in datos:
            archivo.write(linea + '\n')

    print(f"Archivo '{nombre_archivo}' generado exitosamente con {len(datos)} registros.")


# Generar y guardar los datos
if __name__ == "__main__":
    datos_aportes = generar_datos_aportes()
    guardar_archivo_aportes(datos_aportes)