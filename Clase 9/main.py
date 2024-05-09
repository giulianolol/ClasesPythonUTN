"""
En una veterinaria se busca implementar un sistema de registro para llevar un seguimiento
detallado de las mascotas atendidas en el establecimiento. El registro deberá contener la
siguiente información:
● DNI del dueño de la mascota.
● Nombre de la mascota.
● Edad de la mascota.
● Especie de la mascota.
● Sexo de la mascota.
● Peso de la mascota.
● Fecha de la última visita.
● Historial médico.
El programa debe permitir al veterinario:
1. Registrar nuevas mascotas, ingresando todos los datos requeridos.
2. Actualizar la información de una mascota en cada nueva visita, manteniendo un
historial médico completo y actualizado.
Además, se requiere que el sistema proporcione las siguientes funcionalidades:
1. Mostrar información completa de todas las mascotas: Esta función permitirá
visualizar todos los datos registrados de todas las mascotas atendidas en la
veterinaria.
2. Mostrar información completa solo de las mascotas que superen el promedio
de edad: Esta opción mostrará únicamente los datos de las mascotas cuya edad
supere el promedio de edad de todas las mascotas registradas.
3. Calcular el promedio de peso de todas las mascotas: Esta función calculará y
mostrará el promedio de peso de todas las mascotas registradas en la veterinaria.
4. Contar la cantidad de perros registrados: Permitirá obtener el número total de
perros registrados en el sistema.
5. Identificar el tipo de mascota más registrado: Esta función determinará cuál es el
tipo de mascota (perro, gato, ave, etc.) que más se ha registrado en la veterinaria
"""

import datetime
from funciones import *
fecha_hoy = datetime.date.today() #para obtener la fecha de hoy
fecha_formato_perzonalizado = fecha_hoy.strftime("%d/%m/%Y") #para cambiar el formato a dia/mes/año

registro_mascotas = [
    ["12345678", "Luna", 3, "Perro", "Hembra", 8.5, "01/05/2024", "Vacunación anual"],
    ["23456789", "Max", 7, "Gato", "Macho", 5.2, "28/04/2024", "Control de pulgas"],
    ["34567890", "Kiwi", 1, "Dragón", "Hembra", 88000, "02/05/2024", "Recorte de alas"],
    ["45678901", "Rocky", 5, "Perro", "Macho", 12.1, "30/04/2024", "Revisión dental"],
    ["56789012", "Coco", 2, "Gato", "Hembra", 4.8, "03/05/2024", "Desparasitación"]
]

while(True):
    opcion = int(input("Elija una opción.\n1.Registar una mascota.\n2.Dar Consulta Medica.\n3.Mostrar todas las mascotas.\n4.Mostrar solo las mascotas que superan el promedio de edad.\n5.Calcular el promedio de mascotas.\n6.Contar cantida de perros.\n7.Identificar tipo de mascota mas registrado.\n8.Salir."))
    match opcion:
        case 1:
            registrar_mascota(registro_mascotas)
        case 2:
            dar_consulta_medica(registro_mascotas)
        case 3:
            mostrar_todas_las_mascotas(registro_mascotas)
        case 4:
            mostrar_mascotas_que_superan_promedio_edad(registro_mascotas)
        case 5:
            calcular_promedio_mascotas(registro_mascotas)
        case 6:
            calcular_cantida_perros(registro_mascotas)
        case 7:
            identificar_tipo_de_mascota_mas_registrada(registro_mascotas)
        case 8:
            print("Saliendo del sistema.")
            break