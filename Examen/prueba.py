import os
import json
from datetime import datetime

# Función para generar el reporte
def generar_reporte_por_nombre(proyectos, nombre_proyecto, numero_reporte_file="numero_reporte.txt"):
    # Filtrar proyectos que coincidan con el nombre
    proyectos_filtrados = [proyecto for proyecto in proyectos if proyecto['nombre'] == nombre_proyecto]

    # Leer el número de reporte actual desde el archivo (si existe)
    if os.path.exists(numero_reporte_file):
        with open(numero_reporte_file, "r") as f:
            numero_reporte = int(f.read().strip())
    else:
        numero_reporte = 0

    # Incrementar el número de reporte
    numero_reporte += 1

    # Guardar el nuevo número de reporte en el archivo
    with open(numero_reporte_file, "w") as f:
        f.write(str(numero_reporte))

    # Crear el nombre del archivo de reporte
    nombre_archivo_reporte = f"reporte_{numero_reporte}_nombre.txt"

    # Obtener la fecha de solicitud del reporte
    fecha_solicitud = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Contenido del reporte
    contenido_reporte = {
        "numero_reporte": numero_reporte,
        "fecha_solicitud": fecha_solicitud,
        "cantidad_proyectos": len(proyectos_filtrados),
        "proyectos": proyectos_filtrados
    }

    # Escribir el contenido del reporte en el archivo
    with open(nombre_archivo_reporte, "w") as f:
        f.write(json.dumps(contenido_reporte, indent=4))

    print(f"Reporte {numero_reporte} guardado en {nombre_archivo_reporte}")

# Ejemplo de uso
proyectos = [
    {"nombre": "Proyecto A", "presupuesto": 10000},
    {"nombre": "Proyecto B", "presupuesto": 20000},
    {"nombre": "Proyecto C", "presupuesto": 15000},
    {"nombre": "Proyecto D", "presupuesto": 5000}
]

nombre_proyecto = "Proyecto B"

# Generar el reporte
generar_reporte_por_nombre(proyectos, nombre_proyecto)
