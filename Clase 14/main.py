from funciones import *
from datos_muestra import lista_profesores as lista

"""
"id"
"nombre"
"apellido"
"DNI"
"genero"
"edad"
"clases"
"materias"
"activo"
"""

lista_profesores_activos = []
conteo_materias = {}

# for i in range(len(lista)):
    
#     mostar_profesores_activos(lista[i], lista_profesores_activos)

# for i in range(len(lista_profesores_activos)):
    
#     print(lista_profesores_activos[i])


mostrar_profesores_y_materias(lista, conteo_materias)

profesor_modificado = {}



resultado = pedir_id_para_modificar_clase(lista)

print(resultado["clases"])