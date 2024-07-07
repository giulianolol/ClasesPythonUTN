import csv
from datetime import datetime
"""
def cargar_datos(csv_file):
    proyectos = []
    with open(csv_file, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Presupuesto'] = float(row['Presupuesto'])
            row['Fecha de inicio'] = datetime.strptime(row['Fecha de inicio'], '%d/%m/%Y')
            proyectos.append(row)
    return proyectos

def ordenar_proyectos(proyectos, criterio, orden='ascendente'):
    if criterio not in ['Nombre del Proyecto', 'Presupuesto', 'Fecha de inicio']:
        print("Criterio de ordenación no válido.")
        return proyectos
    
    reverse = orden == 'descendente'
    proyectos.sort(key=lambda x: x[criterio], reverse=reverse)
    return proyectos

def mostrar_proyectos(proyectos):
    for proyecto in proyectos:
        print(f"{proyecto['id']}, {proyecto['Nombre del Proyecto']}, {proyecto['Descripcion']}, {proyecto['Fecha de inicio'].strftime('%d-%m-%Y')}, {proyecto['Fecha de Fin']}, {proyecto['Presupuesto']}, {proyecto['Estado']}")

# Cargar datos del CSV
csv_file = 'Proyectos.csv'
proyectos = cargar_datos(csv_file)

# Ordenar y mostrar proyectos por Nombre en orden ascendente
proyectos_ordenados = ordenar_proyectos(proyectos, 'Nombre del Proyecto', 'ascendente')
mostrar_proyectos(proyectos_ordenados)

# Ordenar y mostrar proyectos por Presupuesto en orden descendente
proyectos_ordenados = ordenar_proyectos(proyectos, 'Presupuesto', 'descendente')
mostrar_proyectos(proyectos_ordenados)

# Ordenar y mostrar proyectos por Fecha de inicio en orden ascendente
proyectos_ordenados = ordenar_proyectos(proyectos, 'Fecha de inicio', 'ascendente')
mostrar_proyectos(proyectos_ordenados)
"""

import csv
from datetime import datetime


import csv
from datetime import datetime

def limpiar_fecha(fecha):
    
    #ANOTACIÓN: LA FUNCIÓN ESTÁ ARMADA PARA QUE NO ROMPA ANTE NINGUNA FECHA. NO QUERIA MANIPULAR LOS DATOS DSL CSV MANUALMENTE.
    
    fecha = fecha.strip()
    
    formatos = ['%d-%m-%Y', '%Y-%m-%d', '%d/%m/%Y']
    
    for formato in formatos:
        
        try:
            
            retorno = datetime.strptime(fecha, formato).strftime('%d/%m/%Y')

            return retorno
        
        except ValueError:
            
            continue
        
    raise ValueError(f"Formato de fecha no reconocido: {fecha}")

def cargar_y_formatear_fechas(csv_file):
    
    proyectos = []
    
    with open(csv_file, mode='r', encoding='utf-8-sig') as file:
        
        reader = csv.DictReader(file)
        
        for row in reader:
            
            row['Fecha de inicio'] = limpiar_fecha(row['Fecha de inicio'])
            
            row['Fecha de Fin'] = limpiar_fecha(row['Fecha de Fin'])
            
            proyectos.append(row)
            
    return proyectos

def guardar_datos(csv_file, proyectos):
    
    encabezados = ['id', 'Nombre del Proyecto', 'Descripcion', 'Fecha de inicio', 'Fecha de Fin', 'Presupuesto', 'Estado']
    
    with open(csv_file, mode='w', newline='', encoding='utf-8-sig') as file:
        
        writer = csv.DictWriter(file, fieldnames=encabezados)
        
        writer.writeheader()
        
        for proyecto in proyectos:
            
            writer.writerow(proyecto)

ruta_csv = 'Proyectos.csv'

proyectos = cargar_y_formatear_fechas(ruta_csv)

guardar_datos(ruta_csv, proyectos)
