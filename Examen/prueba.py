import csv
from datetime import datetime

def cargar_datos(csv_file):
    proyectos = []
    with open(csv_file, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Fecha de inicio'] = datetime.strptime(row['Fecha de inicio'].strip(), '%d/%m/%Y')
            proyectos.append(row)
    return proyectos

def burbuja_ordenar_proyectos_por_fecha(proyectos, orden='ascendente'):
    n = len(proyectos)
    for i in range(n):
        for j in range(0, n-i-1):
            if (orden == 'ascendente' and proyectos[j]['Fecha de inicio'] > proyectos[j+1]['Fecha de inicio']) or \
               (orden == 'descendente' and proyectos[j]['Fecha de inicio'] < proyectos[j+1]['Fecha de inicio']):
                # Intercambiar las posiciones
                proyectos[j], proyectos[j+1] = proyectos[j+1], proyectos[j]
    return proyectos

def mostrar_proyectos(proyectos):
    for proyecto in proyectos:
        print(f"{proyecto['id']}, {proyecto['Nombre del Proyecto']}, {proyecto['Descripcion']}, {proyecto['Fecha de inicio'].strftime('%d/%m/%Y')}, {proyecto['Fecha de Fin']}, {proyecto['Presupuesto']}, {proyecto['Estado']}")

# Archivo CSV
csv_file = 'Proyectos.csv'

# Cargar datos del CSV
proyectos = cargar_datos(csv_file)


proyectos_ordenados = burbuja_ordenar_proyectos_por_fecha(proyectos)

# Mostrar proyectos ordenados
mostrar_proyectos(proyectos_ordenados)
