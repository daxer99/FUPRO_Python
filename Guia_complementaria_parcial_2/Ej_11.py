def cargar_datos_lluvias(nombre_archivo):
    """a) Carga y almacena los datos en una lista de listas"""
    datos = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    partes = linea.split('-')
                    if len(partes) == 3:
                        # Cada registro es una lista: [id_localidad, fecha, mm_lluvia]
                        registro = [
                            int(partes[0]),  # id_localidad
                            partes[1],  # fecha
                            float(partes[2])  # mm_lluvia
                        ]
                        datos.append(registro)
        return datos
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
        return []


def calcular_total_lluvia_por_localidad(datos):
    """b) Calcula el total de lluvia por localidad usando listas"""
    # Crear lista para acumular lluvia por localidad (índices 1-10)
    lluvia_localidades = [0] * 11  # índice 0 no se usa, usamos 1-10

    for registro in datos:
        id_localidad = registro[0]  # posición 0: id_localidad
        mm_lluvia = registro[2]  # posición 2: mm_lluvia
        lluvia_localidades[id_localidad] += mm_lluvia

    return lluvia_localidades


def encontrar_localidad_mayor_lluvia(lluvia_localidades):
    """c) Encuentra la localidad con mayor precipitación acumulada"""
    max_lluvia = 0
    id_max_localidad = 0

    for id_localidad in range(1, 11):  # Localidades 1 a 10
        if lluvia_localidades[id_localidad] > max_lluvia:
            max_lluvia = lluvia_localidades[id_localidad]
            id_max_localidad = id_localidad

    return id_max_localidad, max_lluvia


def calcular_porcentaje_sobre_total(lluvia_max, lluvia_total):
    """d) Calcula el porcentaje de la lluvia máxima sobre el total"""
    if lluvia_total == 0:
        return 0
    return (lluvia_max / lluvia_total) * 100


def encontrar_dia_mayor_lluvia(datos):
    """e) Encuentra el día con mayor lluvia usando listas"""
    # Lista para almacenar fechas únicas y sus acumulados
    fechas_unicas = []
    lluvia_por_fecha = []

    for registro in datos:
        fecha = registro[1]  # posición 1: fecha
        mm_lluvia = registro[2]

        # Buscar si la fecha ya existe en nuestra lista
        encontrado = False
        for i in range(len(fechas_unicas)):
            if fechas_unicas[i] == fecha:
                lluvia_por_fecha[i] += mm_lluvia
                encontrado = True
                break

        # Si no existe, agregarla
        if not encontrado:
            fechas_unicas.append(fecha)
            lluvia_por_fecha.append(mm_lluvia)

    # Encontrar el día con mayor lluvia
    if not lluvia_por_fecha:
        return None, 0

    max_lluvia = 0
    dia_max_lluvia = ""

    for i in range(len(fechas_unicas)):
        if lluvia_por_fecha[i] > max_lluvia:
            max_lluvia = lluvia_por_fecha[i]
            dia_max_lluvia = fechas_unicas[i]

    return dia_max_lluvia, max_lluvia


def main():
    # a) Cargar datos
    print("=== ANÁLISIS DE LLUVIAS ENERO 2024 ===\n")
    datos = cargar_datos_lluvias("lluvias_enero.txt")

    if not datos:
        print("No se pudieron cargar los datos.")
        return

    print(f"Registros cargados: {len(datos)}")

    # b) Total de lluvia por localidad
    lluvia_localidades = calcular_total_lluvia_por_localidad(datos)
    print("\n--- TOTAL DE LLUVIA POR LOCALIDAD ---")
    for id_localidad in range(1, 11):
        print(f"Localidad {id_localidad}: {lluvia_localidades[id_localidad]:.2f} mm")

    # c) Localidad con mayor lluvia
    id_max_localidad, max_lluvia = encontrar_localidad_mayor_lluvia(lluvia_localidades)
    print(f"\n--- LOCALIDAD CON MAYOR PRECIPITACIÓN ---")
    print(f"Localidad {id_max_localidad}: {max_lluvia:.2f} mm")

    # d) Porcentaje sobre el total
    lluvia_total = sum(lluvia_localidades[1:])  # Sumar localidades 1-10
    porcentaje = calcular_porcentaje_sobre_total(max_lluvia, lluvia_total)
    print(f"\n--- PORCENTAJE SOBRE EL TOTAL ---")
    print(f"La localidad {id_max_localidad} representa el {porcentaje:.2f}% del total provincial")
    print(f"Lluvia total provincial: {lluvia_total:.2f} mm")

    # e) Día con mayor lluvia
    dia_max, lluvia_dia_max = encontrar_dia_mayor_lluvia(datos)
    print(f"\n--- DÍA CON MAYOR LLUVIA ---")
    print(f"Fecha: {dia_max} - Lluvia: {lluvia_dia_max:.2f} mm")


if __name__ == "__main__":
    main()