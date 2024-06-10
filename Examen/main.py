from funciones import *

archivo_csv = 'Proyectos.csv'

# lista_archivo = leer_csv(archivo_csv)
    
# contar_proyectos_activos(lista_archivo)

dicio = {'id': 15,'Nombre del Proyecto': "Prueba",'Descripcion': "Descripcion Prueba",'Fecha de inicio' : 321,"Fecha de Fin": 546,'Presupuesto': 987897,'Estado':"Activo"}

escribir_csv(dicio) 

print(leer_csv('Proyectos.csv'))

