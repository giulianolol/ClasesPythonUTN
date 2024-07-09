import csv, json, os
import re
import time
from datetime import datetime

def contar_proyectos_activos(lista: list):

    contador = 0
    
    for i in range(len(lista)):
        
        if lista[i]["Estado"] == "Activo":
            
            contador +=1

            if contador == 50:
                
                print("Ya llegaste al límite de 50 proyectos activos, elimina alguno para continuar.")
                break
    
    if contador < 50:
        
        print("Todo ok")

def cargar_csv_lista(ruta):
    
    with open(ruta, mode='r', newline='', encoding='utf-8-sig') as archivo:
        
        lector = csv.DictReader(archivo)
        
        return list(lector)

def escribir_csv(ruta_archivo, datos):
    
    headers = datos[0].keys()
    
    with open(ruta_archivo, mode='w', newline='', encoding='utf-8-sig') as file:
        
        writer = csv.DictWriter(file, fieldnames=headers)
        
        writer.writeheader()
        
        writer.writerows(datos)

def leer_json(ruta_json):
    
    archivo_json = open(ruta_json, 'r')
    
    datos = json.load(archivo_json)
    
    archivo_json.close()
    
    return datos

def escribir_json(id, nombre_proyecto, descripcion, fecha_de_inicio, fecha_de_fin, presupuesto, estado):
    
    datos = leer_json('ProyectosFinalizados.json')
    
    proyectos_finalizados = {'id': id, 'Nombre del Proyecto': nombre_proyecto, 'Descripcion':descripcion, 'Fecha de incio': fecha_de_inicio, 'Fecha de Fin': fecha_de_fin, 'Presupuesto': presupuesto, 'Estado': estado,}
    
    datos["ProyectosFinalizados"].append(proyectos_finalizados)
                    
    with open("ProyectosFinalizados.json", "w") as file:
                        
        json.dump(datos, file, indent=4)
    
    file.close()

def validar_ingreso_palabra(cadena):
    
    retorno = True
    
    for i in cadena:
        
        if i.isalpha() == False and i != " ":
            
            retorno = False
            break       
    
    return retorno

def validar_ingreso_numero_entero(numero:float):
    
    retorno = False
    
    if type(numero) != float:
    
        for i in numero:
            
            if i.isalpha() == True or i == "." or i =="," or i == "/":
                
                retorno = True
                break
    else:
        
        retorno = True
    
    return retorno
         
def validar_ingreso_alfanumerico(string:str):
    
    retorno = True
    
    for i in string:
        
        if i.isalnum() == False and i != " ":
            
            retorno = False
            break
    
    return retorno 

def validar_formato_fechas(fecha):
    
    contador = 0
    
    for i in fecha:
        
        if i == "/":
            
            contador +=1
    
    if contador == 2 and len(fecha) == 10:
    
        retorno = True
        bandera = False
        
        partes = fecha.split('/')
        
        partes_aux = fecha.split('/')
        
        if len(partes) != 3:
            retorno =  False
            
        elif not (partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit()):
            retorno = False
            bandera = True
        
        elif len(partes[0]) != 2 or len(partes[1]) != 2 or len(partes[2]) != 4:
            
            retorno = False
        
        if bandera == True:
            
            partes_aux[0] = int(partes_aux[0])
            partes_aux[1] = int(partes_aux[1])
            partes_aux[2] = int(partes_aux[2])
            
            if (partes_aux[0] < 1 or partes_aux[0] > 31) or (partes[1] < 1 or partes[1] > 12) or partes[2] < 0:
                
                retorno = False
                
    else: retorno = False
        
    return retorno

def convertir_fecha(fecha):

    retorno = datetime.strptime(fecha, '%d/%m/%Y')
    
    retorno = str(retorno)
     
    retorno = retorno.replace('00:00:00','')

    retorno = retorno.replace('-','/')
    
    retorno = retorno.split('/')

    retorno_aux = retorno[0]
    
    retorno[0] = retorno[2]
    
    retorno[2] = retorno_aux
    
    retorno = '/'.join([fecha.strip() for fecha in retorno])
    
    return retorno

def fechas_validas(fecha1, fecha2):
    
    retorno = True
    
    if not (validar_formato_fechas(fecha1) and validar_formato_fechas(fecha2)):
        
        retorno = (False, "Formato de fecha incorrecto")
        
    fecha1 = convertir_fecha(fecha1)
    fecha2 = convertir_fecha(fecha2)
    
    if fecha1 >= fecha2:
        
        retorno = (False, "La fecha de fin es menor a al fecha inicio.")
    
    return retorno

def obtener_nombre(proyecto,i):
    
    retorno = proyecto[i]["Nombre del Proyecto"].lower()
    
    return retorno

def obtener_presupuesto(proyecto,i):
    
    retorno = float(proyecto[i]["Presupuesto"])
    
    return retorno

def validar_agregar_proyecto():
    
    bandera_proyecto = False
    bandera_fecha = False

    datos = cargar_csv_lista('Proyectos.csv')
    
    nombre_proyecto = input("Ingrese el nombre del proyecto: ")
    
    validacion_nombre_proyecto = validar_ingreso_palabra(nombre_proyecto)
    
    while validacion_nombre_proyecto == False or len(nombre_proyecto) > 30 or nombre_proyecto == '': 
        
        nombre_proyecto = input("Error, ingrese un nombre válido, menor a 30 caracteres: ")

        validacion_nombre_proyecto = validar_ingreso_palabra(nombre_proyecto)
    
    descripcion_proyecto = input("Ingrese la descripcion del proyecto: ")
    
    validacion_descripcion_proyecto = validar_ingreso_alfanumerico(descripcion_proyecto)
    
    while validacion_descripcion_proyecto == False or len(descripcion_proyecto) > 200 or descripcion_proyecto == '':
        
        descripcion_proyecto = input("Error, debe ingresar una descripción válida. Solo caracteres alfanumeros y que no superen los 200 digitos.")
        
        validacion_descripcion_proyecto = validar_ingreso_alfanumerico(descripcion_proyecto)
    
    while bandera_proyecto == False:
        
        presupesto_proyecto = input("Ingrese el presupesto para el proyecto: ")
        
        validacion_presupuesto_proyecto = validar_ingreso_numero_entero(presupesto_proyecto)

        while validacion_presupuesto_proyecto == True or presupesto_proyecto == "":
            
            presupesto_proyecto = input("Error, debe ingresar un número entero: ")
            
            validacion_presupuesto_proyecto = validar_ingreso_numero_entero(presupesto_proyecto)
            
        presupesto_proyecto = int(presupesto_proyecto)
        
        if presupesto_proyecto < 500000:
            
            print("Error, ingrese un presupesto mayor a 500000: ")
            
            continue
        
        bandera_proyecto = True
        
    
    while bandera_fecha == False:
        
        fecha_inicio = input("Ingrese la fecha de inicio del proyecto: ")
        
        validacion_formato_fecha = validar_formato_fechas(fecha_inicio)
        
        while validacion_formato_fecha == False:
        
            fecha_inicio = input("Error, la fecha tiene que tener una fecha valida y tiene que tener el siguiente formato. 'DD/MM/AAAA'")
        
            validacion_formato_fecha = validar_formato_fechas(fecha_inicio)
        
        fecha_inicio_formateada = convertir_fecha(fecha_inicio)
        
        bandera_fecha = True
    
    bandera_fecha = False
    
    while bandera_fecha == False:
        
        fecha_fin = input("Ingrese la fecha de fin del proyecto: ")
        
        validacion_formato_fecha = validar_formato_fechas(fecha_fin)
        
        while validacion_formato_fecha == False:
            
            fecha_fin = input("Error, la fecha tiene que tener el siguiente formato. 'DD/MM/AAAA'")
            
            validacion_formato_fecha = validar_formato_fechas(fecha_fin)
            
        fecha_fin_formateada = convertir_fecha(fecha_fin)
        
        if fecha_fin_formateada < fecha_inicio_formateada:
            
            print("Error, la fecha de fin es anterior a la fecha de inicio.")
                    
            continue
           
        bandera_fecha = True
                                    
    estado_proyecto = input("Ingrese el estado del proyecto(Activo/Cancelado/Finalizado): ").capitalize()
    
    while estado_proyecto != "Activo" and estado_proyecto != "Cancelado" and estado_proyecto != "Finalizado":
        
        estado_proyecto = input("Error, el estado solo puede ser Activo, Cancelado o Finalizado.").capitalize()
    
    ultimo_id = int(datos[-1]['id']) if datos else 0
    
    proyecto = {'id':ultimo_id + 1,'Nombre del Proyecto':nombre_proyecto, 'Descripcion': descripcion_proyecto, 'Presupuesto':presupesto_proyecto,'Fecha de inicio': fecha_inicio, 'Fecha de Fin': fecha_fin, 'Estado': estado_proyecto}
    
    lista_proyectos = cargar_csv_lista('Proyectos.csv')
    
    lista_proyectos.append(proyecto)
    
    escribir_csv('Proyectos.csv', lista_proyectos)
    
    return proyecto
    
def modificar_proyecto(lista_proyectos:list):
    
    bandera_id_encontado = False
    
    for i in lista_proyectos:
        
        for key , value in  i.items():
        
            print(key, value)
        
        print("----------------------------------")
      
    id = input("Ingrese el id del proyecto a modificar: ")
        
    validacion_id = validar_ingreso_numero_entero(id)
        
    while validacion_id == True:
            
        id = input("Error, ingres un valor numérico.")
            
        validacion_id = validar_ingreso_numero_entero(id)
        
    for i in range(len(lista_proyectos)):
        
        if lista_proyectos[i]["id"] == id:
            
            proyecto_diccionario = lista_proyectos[i] 
            bandera_id_encontado = True
    
    if bandera_id_encontado == True:
        
        imprimir_sub_menu(lista_proyectos, id)
    
    else: 
        
        print("Error, id no encontrado.")

def imprimir_sub_menu(lista_proyectos:list, id:int):
    
    print("Mostrando datos de proyecto acutual...")
    
    lista_posibles_valores = ["1", "2", "3", "4", "5", "6"]
    
    print(lista_proyectos)
    
    for proyecto in lista_proyectos:
        
        if proyecto['id'] == id:
            
            proyecto_aux = proyecto
            
            proyecto_a_modificar = proyecto
            
            for key, value in proyecto.items():
                    
                print(f"{key} - {value}")
        
    valor = input("*********************************************\n|- 1. Nombre del Proyecto.\n|- 2. Descripción.\n|- 3. Fecha de inicio.\n|- 4. Fecha de Fin.\n|- 5. Presupesto.\n|- 6. Estado.")
    
    validar_valor = validar_ingreso_numero_entero(valor)
    
    while validar_valor == True or valor not in lista_posibles_valores:    
            
        valor = input("Error, el valor ingresado no es válido. Tiene que ser un valor numérico y ser un valor entre el 1 y el 6.")
            
        validar_valor = validar_ingreso_numero_entero(valor)
    
    match valor:
        
        case "1":
            
            nombre_anterior =  proyecto_aux["Nombre del Proyecto"]
            
            nombre_proyecto = input("Ingrese el nuevo nombre del proyecto: ")
    
            validacion_nombre_proyecto = validar_ingreso_palabra(nombre_proyecto)
    
            while validacion_nombre_proyecto == False or len(nombre_proyecto) > 30:
        
                nombre_proyecto = input("Error, ingrese un nombre válido, menor a 30 caracteres: ")

                validacion_nombre_proyecto = validar_ingreso_palabra(nombre_proyecto)
            
            proyecto_a_modificar["Nombre del Proyecto"] = nombre_proyecto
            
            for proyecto in lista_proyectos:
                
                if proyecto_a_modificar['id'] == id:
                    
                    proyecto = proyecto_a_modificar
            
            escribir_csv('Proyectos.csv', lista_proyectos)
            
            print(f"El nombre se modificó correctamente.\n|- Nombre anterior: {nombre_anterior}\n|- Nombre actualizado: {proyecto_a_modificar['Nombre del Proyecto']}")
            
            tecla = input("Ingrese una tecla para continuar.")
        
        case "2":
            
            descripcion_anterior = proyecto_aux["Descripcion"]
            
            descripcion_proyecto = input("Ingrese la nueva descripcón del proyecto: ")
            
            validacion_descripcion_proyecto = validar_ingreso_alfanumerico(descripcion_proyecto)
    
            while validacion_descripcion_proyecto == False or len(descripcion_proyecto) > 200:
        
                descripcion_proyecto = input("Error, debe ingresar una descripción válida. Solo caracteres alfanumeros y que no superen los 200 digitos.")
        
                validacion_descripcion_proyecto = validar_ingreso_alfanumerico(descripcion_proyecto)
            
            proyecto_a_modificar["Descripcion"] = descripcion_proyecto
            
            for proyecto in lista_proyectos:
                
                if proyecto_a_modificar['id'] == id:
                    
                    proyecto = proyecto_a_modificar
            
            escribir_csv('Proyectos.csv', lista_proyectos)
            
            print(f"La descripcion se modificó correctamente.\n|- Descripcion anterior: {descripcion_anterior}\n|- Descripcion actualizada: {proyecto_a_modificar['Descripcion']}")
                         
            tecla = input("Ingrese una tecla para continuar.")        
            
        case "3":
            
            bandera_fecha = False
            
            fecha_inicio_anterior = proyecto_aux["Fecha de inicio"]
            
            while bandera_fecha == False:
        
                fecha_inicio = input("Ingrese la nueva fecha de inicio del proyecto: ")
        
                validacion_formato_fecha = validar_formato_fechas(fecha_inicio)
                
                bandera_fecha = True
        
            while validacion_formato_fecha == False:
        
                fecha_inicio = input("Error, la fecha tiene que tener el siguiente formato. 'DD/MM/AAAA'")
        
                validacion_formato_fecha = validar_formato_fechas(fecha_inicio)
        
            fecha_inicio_formateada = convertir_fecha(fecha_inicio)
            
            proyecto_a_modificar["Fecha de inicio"] = fecha_inicio_formateada
            
            for proyecto in lista_proyectos:
                
                if proyecto_a_modificar['id'] == id:
                    
                    proyecto = proyecto_a_modificar
            
            escribir_csv('Proyectos.csv', lista_proyectos)
            
            print(f"La fecha se modificó correctamente.\n|- Fecha anterior: {fecha_inicio_anterior}\n|- Fecha actualizada: {proyecto_a_modificar['Fecha de inicio']}")
                         
            tecla = input("Ingrese una tecla para continuar.")
                  
        case "4":
            
            bandera_fecha = False
            
            fecha_fin_anterior = proyecto_aux["Fecha de Fin"]
            
            while bandera_fecha == False:
        
                fecha_fin = input("Ingrese la nueva fecha de fin del proyecto: ")
        
                validacion_formato_fecha = validar_formato_fechas(fecha_fin)
                
                bandera_fecha = True
        
            while validacion_formato_fecha == False:
        
                fecha_fin = input("Error, la fecha tiene que tener el siguiente formato. 'DD/MM/AAAA'")
        
                validacion_formato_fecha = validar_formato_fechas(fecha_fin)
        
            fecha_fin_formateada = convertir_fecha(fecha_fin)
            
            proyecto_a_modificar["Fecha de Fin"] = fecha_fin_formateada
            
            for proyecto in lista_proyectos:
                
                if proyecto_a_modificar['id'] == id:
                    
                    proyecto = proyecto_a_modificar
        
            escribir_csv('Proyectos.csv', lista_proyectos)
            
            print(f"La fecha se modificó correctamente.\n|- Fecha anterior: {fecha_fin_anterior}\n|- Fecha actualizada: {proyecto_a_modificar['Fecha de Fin']}")
                         
            tecla = input("Ingrese una tecla para continuar.") 
        
        case "5":
            
            bandera_proyecto = False
            presupuesto_anterior = proyecto_aux["Presupuesto"]
            
            while bandera_proyecto == False:
        
                presupesto_proyecto = input("Ingrese el nuevo presupesto para el proyecto: ")
        
                validacion_presupuesto_proyecto = validar_ingreso_numero_entero(presupesto_proyecto)

                while validacion_presupuesto_proyecto == True:
            
                    presupesto_proyecto = input("Error, debe ingresar un número entero: ")
            
                    validacion_presupuesto_proyecto = validar_ingreso_numero_entero(presupesto_proyecto)
            
                presupesto_proyecto = int(presupesto_proyecto)
        
                if presupesto_proyecto < 500000:
            
                    print("Error, ingrese un presupesto mayor a 500000: ")
                
                else:
                
                    bandera_proyecto = True
                
            proyecto_a_modificar["Presupuesto"] = presupesto_proyecto
            
            for proyecto in lista_proyectos:
                
                if proyecto_a_modificar['id'] == id:
                    
                    proyecto = proyecto_a_modificar
            
            escribir_csv('Proyectos.csv', lista_proyectos)
            
            print(f"El presupuesto se modificó correctamente.\n|- Presupuesto anterior: {presupuesto_anterior}\n|- Precupesto actualizado: {proyecto_a_modificar['Presupuesto']}")       
                    
            tecla = input("Ingrese una tecla para continuar.")
        
        case "6":
            
            estado_anterior = proyecto_aux["Estado"]
            
            estado_proyecto = input("Ingrese el nuevo estado del proyecto: ")
            
            while estado_proyecto != "Activo" and estado_proyecto != "Cancelado" and estado_proyecto and "Finalizado":
        
                estado_proyecto = input("Error, el estado solo puede ser Activo, Cancelado o Finalizado.").capitalize()
            
            for proyecto in lista_proyectos:
                
                if proyecto_a_modificar['id'] == id:
                    
                    proyecto = proyecto_a_modificar
            
            escribir_csv('Proyectos.csv', lista_proyectos)
            
            print(f"El estado se modificó correctamente.\n|- Estado anterior: {estado_anterior}\n|- Estado actualizado: {proyecto_a_modificar['Estado']}")
                    
            tecla = input("Ingrese una tecla para continuar.")
            
def comprobar_proyectos():
    
    lista_proyectos = cargar_datos_fin('Proyectos.csv')
    
    fecha_hoy = datetime.today()
        
    for proyecto in lista_proyectos:
            
        if proyecto['Fecha de Fin'] < fecha_hoy:
                
            proyecto['Estado'] = 'Finalizado'
            
            print("ENCONTRÉ")

    guardar_datos('Proyectos.csv', lista_proyectos)
    
    return lista_proyectos

def cargar_datos_fecha_fin(csv_file):
    
    proyectos = []
    
    with open(csv_file, mode='r', encoding='utf-8-sig') as file:
        
        reader = csv.DictReader(file)
        
        for row in reader:
            
            row['Fecha de Fin'] = datetime.strptime(row['Fecha de Fin'].strip(), '%d/%m/%Y')
            
            proyectos.append(row)
            
    return proyectos

def actualizar_estados(proyectos):
    
    fecha_actual = datetime.now()
    
    for proyecto in proyectos:
        
        if proyecto['Fecha de Fin'] < fecha_actual:
            
            proyecto['Estado'] = 'Finalizado'
            
    return proyectos

def guardar_datos_fecha_fin(csv_file, proyectos):
    
    fieldnames = ['id', 'Nombre del Proyecto', 'Descripcion', 'Fecha de inicio', 'Fecha de Fin', 'Presupuesto', 'Estado']
    
    with open(csv_file, mode='w', newline='', encoding='utf-8-sig') as file:
        
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for proyecto in proyectos:

            proyecto['Fecha de Fin'] = proyecto['Fecha de Fin'].strftime('%d/%m/%Y')
            
            writer.writerow(proyecto)   
                   
def cancelar_proyecto(lista_proyectos):
    
    datos = cargar_csv_lista('Proyectos.csv')
    
    bandera_id_encontado = False
      
    id = input("Ingrese el id del proyecto a cancelar: ")
        
    validacion_id = validar_ingreso_numero_entero(id)
        
    while validacion_id == True:
            
        id = input("Error, ingres un valor numérico.")
            
        validacion_id = validar_ingreso_numero_entero(id)
        
    for i in range(len(lista_proyectos)):
        
        if lista_proyectos[i]["id"] == id:
            
            proyecto_aux = lista_proyectos[i]
            proyecto_diccionario = lista_proyectos[i] 
            bandera_id_encontado = True
    
    if bandera_id_encontado == True:
        
        print(f"Seguro desea cancelar el siguiente proyecto: ")
        
        for key, value in proyecto_diccionario.items():
            
            print(f"{key} - {value}")
        
        tecla = input("\n1. Si.  -  2. No.")
        
        if tecla == "1":
            
            proyecto_diccionario["Estado"] = "Cancelado"

            print(f"El proyecto numero {proyecto_diccionario['id']} fue cancelado satisfactoriamente.")
            
            for i in lista_proyectos:
                
                if i['id'] == id:
                    
                    i['Estado'] = proyecto_diccionario['Estado']
            
            escribir_csv('Proyectos.csv', lista_proyectos)
                    
            
            for key, value in proyecto_diccionario.items():
            
                print(f"{key} - {value}")
        
        else:
            
            print("Ningún proyecto fué cancelado.")

    else:
        
        ultimo_id = int(datos[-1]['id']) if datos else 0

        print(f"El id ingresado no está asignado a ningún proyecto. El último proyecto tiene el id {ultimo_id}")

def mostrar_todos(lista_proyectos):
    
    print("___________________________________________________________________________________________________________________________________________________________________________\n| Nombre del Proyecto | Descripción | Presupuesto | Fecha de Inicio | Fecha de Fin | Estado |")
    
    for proyecto in lista_proyectos:
        
        nombre = proyecto['Nombre del Proyecto']
        descripcion = proyecto['Descripcion']
        presupuesto = f"${proyecto['Presupuesto']}"
        fecha_inicio = proyecto['Fecha de inicio']
        fecha_fin = proyecto['Fecha de Fin']
        estado = proyecto['Estado']
        
        print(f"| {nombre} | {descripcion} | {presupuesto} | {fecha_inicio} | {fecha_fin} | {estado} |")

    print("___________________________________________________________________________________________________________________________________________________________________________")

def calcular_promedio(lista, key):
    
    suma = 0
    
    for i in range(len(lista)):
        
        num_aux = lista[i][key]
        
        num_aux = float(num_aux)
        
        suma += num_aux
        
    return suma / len(lista)

def buscar_proyecto_por_nombre(lista_proyecto):
    
    nombre = input("Ingrese el nombre del proyecto a buscar: ").lower()
    
    for i in range(1,(len(lista_proyecto))):
        
        nombre_lower = lista_proyecto[i]["Nombre del Proyecto"]
        
        nombre_lower = nombre_lower.lower()
        
        if nombre_lower == nombre:
            
            retorno =  lista_proyecto[i]
            
            break
        
        else: retorno = "No hay ningún proyecto con ese nombre"
        
    return retorno

def ordenar_y_mostrar_proyectos(lista_proyectos:list):
    
    criterio = input("Ingres el criterio por el cual desea ordenar los proyectos:\n| 1. Nombre.\n| 2. Presupuesto.\n| 3. Fecha de inicio.\n")
    
    while criterio != "1" and criterio != "2" and criterio != "3":
        
        criterio = input("Error, ingrese un valor válido:\n| 1. Nombre.\n| 2. Presupuesto.\n| 3. Fecha de inicio.\n")
    
    criterio_2 = input("Ingrese un 1 si quiere ordenarla de manera ascendente o 2 si quiere hacerlo de manera descendente: ")
    
    while criterio_2 != "1" and criterio_2 != "2":
        
        criterio_2 = input("Error, ingrese un valor válido: ")
    
    
    if criterio_2 == "1":
        
        criterio_2 = True
    
    else: criterio_2 = False
    
    if criterio == "1":
        
        clave = lambda proyecto: proyecto['Nombre del Proyecto']
        
        lista_ordenada = sorted(lista_proyectos, key=clave, reverse = criterio_2)
    
        for proyecto in lista_ordenada:
            
            print(f"{proyecto['id']} - {proyecto['Nombre del Proyecto']} - {proyecto['Descripcion']} - {proyecto['Fecha de inicio']} - {proyecto['Fecha de Fin']} - {proyecto['Presupuesto']} - {proyecto['Estado']}")
            
            print('----------------------------------------------------------------')
        
    elif criterio == "2":
        
       lista_proyectos = burbujeo_ordenar_presupuesto(lista_proyectos, criterio_2)
       
       for proyecto in lista_proyectos:
        
            print(f"{proyecto['id']} - {proyecto['Nombre del Proyecto']} - {proyecto['Descripcion']} - {proyecto['Fecha de inicio']} - {proyecto['Fecha de Fin']} - {proyecto['Presupuesto']} - {proyecto['Estado']}")
            
            print('----------------------------------------------------------------')
    
    elif criterio == "3":
        
        proyectos_ordenados = burbujeo_ordenar_proyectos_por_fecha(lista_proyectos, criterio_2)
        
        for proyecto in proyectos_ordenados:
        
            print(f"{proyecto['id']}, {proyecto['Nombre del Proyecto']}, {proyecto['Descripcion']}, {proyecto['Fecha de inicio'].strftime('%d/%m/%Y')}, {proyecto['Fecha de Fin']}, {proyecto['Presupuesto']}, {proyecto['Estado']}")

def proyectos_inicados_en_invierno(lista_proyectos):
    
    lista_proyectos_iniciados_en_invierno = []
                
    for i in range(len(lista_proyectos)):
                    
        fecha = lista_proyectos[i]["Fecha de inicio"]
                    
        partes = fecha.split("/")
                    
        partes[0] = int(partes[0])
                    
        partes[1] = int(partes[1])
                    
        partes[2] = int(partes[2])
                    
        if partes[1] == 6 and partes[0] >= 21:
                            
            lista_proyectos_iniciados_en_invierno.append(lista_proyectos[i])
                    
        elif partes[1] >= 7 and partes[1] <= 8:
                        
            lista_proyectos_iniciados_en_invierno.append(lista_proyectos[i])
                        
        elif partes[1] == 9 and partes[0] <= 22:
                        
            lista_proyectos_iniciados_en_invierno.append(lista_proyectos[i])
    
    return lista_proyectos_iniciados_en_invierno

def obtener_presupuesto_mayor(lista_proyectos):
    
    bandera = False
    proyectos_prespupuesto_maximo = []
    
    for i in range(len(lista_proyectos)):

        if bandera == False:
            
            maximo = float(lista_proyectos[i]["Presupuesto"])
            
            proyectos_prespupuesto_maximo.append(lista_proyectos[i])

            bandera = True
        
        else:
            
            if float(lista_proyectos[i]["Presupuesto"]) > maximo:
            
                if len(proyectos_prespupuesto_maximo) == 0:
                
                    maximo = float(lista_proyectos[i]["Presupuesto"])
                
                    proyectos_prespupuesto_maximo.append(lista_proyectos[i])
                
                elif len(proyectos_prespupuesto_maximo) > 0:
                    
                    if lista_proyectos[i]["Presupuesto"] > proyectos_prespupuesto_maximo[0]["Presupuesto"]:
                    
                        proyectos_prespupuesto_maximo.clear()
                        
                        proyectos_prespupuesto_maximo.append(lista_proyectos[i]["Presupuesto"])
    
    return proyectos_prespupuesto_maximo

def ordenar_por_presupuesto(lista_proyectos):
    
    for proyecto in lista_proyectos:
        
        proyecto['Presupuesto'] = float(proyecto['Presupuesto'])
        
    proyectos_ordenados = sorted(lista_proyectos, key = lambda y: y['Presupuesto'], reverse = True)
    
    proyectos_ordenados_filtrados = proyectos_ordenados[:3]
    
    return proyectos_ordenados_filtrados
        
def dar_alta_proyecto_cancelado(lista_proyectos):
    
    bandera_pryecto_encontrado = False
    
    id_ingresado = input("Ingrese el id del proyecto que desa dar de alta: ")
    
    for i in range(len(lista_proyectos)):
        
        
        if lista_proyectos[i]['id'] == id_ingresado and lista_proyectos[i]['Estado'] == 'Cancelado':
            
            proyecto_guardado = lista_proyectos[i]
            
            bandera_pryecto_encontrado = True
            
        else: 
            
            retorno = "No se encontró ningún proyecto asociado a este id o su estado no es 'Cancelado'"
    
    if bandera_pryecto_encontrado == True:
        
        print("Proyecto a modificar: ")
        
        for key, value in proyecto_guardado.items():
                    
            if key != "Presupuesto":
                    
                print(f"{key} - {value}")
                    
            else: print(f"{key} - ${value}")
        
        tecla = input("Presiona 1 si quiere modificar este proyecto, 2 si quiere cancelar: ")
        
        if tecla == "1":
            
            for proyecto in lista_proyectos:
                
                if proyecto['id'] == id_ingresado:
                    
                    proyecto['Estado'] = "Activo"
                    
                    print(proyecto)
                    
            escribir_csv('Proyectos.csv', lista_proyectos)
        
            print("El estado del proyecto se modificó a 'Activo'. ")
            
        else: print("Proceso cancelado.")
            
    else: 
        
        print(retorno)

def obtener_proyectos_inactivos(lista_proyectos):
    
    lista_proyectos_inactivos = []
    
    for i in range(len(lista_proyectos)):
        
        if lista_proyectos[i]["Estado"] != "Activo":
            
            lista_proyectos_inactivos.append(lista_proyectos[i])
    
    return lista_proyectos_inactivos

def cargar_datos(csv_file):
    
    proyectos = []
    
    with open(csv_file, mode='r', encoding='utf-8-sig') as file:
        
        reader = csv.DictReader(file)
        
        for fila in reader:
            
            fila['Fecha de inicio'] = datetime.strptime(fila['Fecha de inicio'].strip(), '%d/%m/%Y')
            
            proyectos.append(fila)
            
    return proyectos

def cargar_datos_fin(csv_file):
    
    proyectos = []
    
    with open(csv_file, mode='r', encoding='utf-8-sig') as file:
        
        reader = csv.DictReader(file)
        
        for row in reader:
            
            row['Fecha de Fin'] = datetime.strptime(row['Fecha de Fin'].strip(), '%d/%m/%Y')
            
            proyectos.append(row)
            
    return proyectos

def burbujeo_ordenar_presupuesto(proyectos, orden):
    
    largo_proyectos = len(proyectos)
    
    if orden == True:
    
        for i in range(largo_proyectos):
            
            for j in range(0, largo_proyectos-i-1):
                
                if proyectos[j]['Presupuesto'] > proyectos[j+1]['Presupuesto']:
                    
                    proyectos[j], proyectos[j+1] = proyectos[j+1], proyectos[j]
    
    else: 
        for i in range(largo_proyectos):
            
            for j in range(0, largo_proyectos-i-1):
                
                if proyectos[j]['Presupuesto'] < proyectos[j+1]['Presupuesto']:
                    
                    proyectos[j], proyectos[j+1] = proyectos[j+1], proyectos[j]
                
    return proyectos

def burbujeo_ordenar_proyectos_por_fecha(proyectos, valor):
    
    largo_lista = len(proyectos)
    
    if valor == True:
    
        orden='ascendente'
    
    else: orden='descendente'
    
    for i in range(largo_lista):
        
        for j in range(0, largo_lista-i-1):
            
            if (orden == 'ascendente' and proyectos[j]['Fecha de inicio'] > proyectos[j+1]['Fecha de inicio']) or (orden == 'descendente' and proyectos[j]['Fecha de inicio'] < proyectos[j+1]['Fecha de inicio']):

                proyectos[j], proyectos[j+1] = proyectos[j+1], proyectos[j]
                
    return proyectos

def limpiar_fecha(fecha):
    
    fecha = fecha.strip()
    
    formatos = ['%d-%m-%Y', '%Y-%m-%d', '%d/%m/%Y']
    
    for formato in formatos:
        
        try:
            
            return datetime.strptime(fecha, formato).strftime('%d/%m/%Y')
        
        except ValueError:
            
            continue
        
    raise ValueError(f"Formato de fecha no reconocido: {fecha}")

def cargar_y_formatear_fechas(csv_file):
    
    proyectos = []
    
    with open(csv_file, mode='r', encoding='utf-8-sig') as file:
        
        reader = csv.DictReader(file)
        
        for fila in reader:
            
            fila['Fecha de inicio'] = limpiar_fecha(fila['Fecha de inicio'])
            
            fila['Fecha de Fin'] = limpiar_fecha(fila['Fecha de Fin'])
            
            proyectos.append(fila)
            
    return proyectos

def guardar_datos(csv_file, proyectos):
    
    fieldnames = ['id', 'Nombre del Proyecto', 'Descripcion', 'Fecha de inicio', 'Fecha de Fin', 'Presupuesto', 'Estado']
    
    with open(csv_file, mode='w', newline='', encoding='utf-8-sig') as file:
        
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for proyecto in proyectos:
            
            writer.writerow(proyecto)

def filtrar_proyectos_por_presupuesto(prespuesto):

    proyectos_presupuesto_mayor = []

    lista_csv = cargar_csv_lista('Proyectos.csv')

    for i in lista_csv:
        
        if float(i['Presupuesto']) > prespuesto: 
            
            proyectos_presupuesto_mayor.append(i)
    
    return proyectos_presupuesto_mayor

def generar_reporte(proyectos, numero_reporte_file = 'numero_reporte_proyectos.txt'):

    if os.path.exists(numero_reporte_file):
        
        with open(numero_reporte_file, "r") as f:
            
            numero_reporte = int(f.read().strip())
    else:
        numero_reporte = 0

    numero_reporte += 1

    with open(numero_reporte_file, "w") as f:
        
        f.write(str(numero_reporte))

    nombre_archivo_reporte = f"reporte_{numero_reporte}_proyectos.txt"

    fecha_solicitud = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    contenido_reporte = {
        "numero_reporte": numero_reporte,
        "fecha_solicitud": fecha_solicitud,
        "cantidad_proyectos": len(proyectos),
        "proyectos": proyectos
    }

    with open(nombre_archivo_reporte, "w") as f:
        
        f.write(json.dumps(contenido_reporte, indent=4))

    print(f"Reporte {numero_reporte} guardado en {nombre_archivo_reporte}")    

def generar_reporte_por_nombre(proyectos, nombre_proyecto, numero_reporte_file="numero_reporte_nombre.txt"):
    
    proyectos_filtrados = []
    
    for proyecto in proyectos:
        
        if proyecto['Nombre del Proyecto'] == nombre_proyecto:
            
            proyectos_filtrados.append(proyecto)

    if os.path.exists(numero_reporte_file):
        
        with open(numero_reporte_file, "r") as file:
            
            numero_reporte = int(file.read().strip())         
    else:
        
        numero_reporte = 0

    numero_reporte += 1

    with open(numero_reporte_file, "w") as file:
        
        file.write(str(numero_reporte))

    nombre_archivo_reporte = f"reporte_{numero_reporte}_nombre.txt"

    fecha_solicitud = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    contenido_reporte = {
        "numero_reporte": numero_reporte,
        "fecha_solicitud": fecha_solicitud,
        "nombre_proyecto": proyectos_filtrados
    }

    with open(nombre_archivo_reporte, "w") as file:
        
        file.write(json.dumps(contenido_reporte, indent=4))

    print(f"Reporte {numero_reporte} guardado en {nombre_archivo_reporte}")    

def imprimir_menu():

    print("*********************************************\n|- 1. Ingresar proyecto.\n|- 2. Modificar proyecto.\n|- 3. Cancelar proyecto.\n|- 4. Comprobar proyectos.\n|- 5. Mostrar todos.\n|- 6. Calcular presupuesto promedio.\n|- 7. Buscar proyecto por nombre.\n|- 8. Ordenar proyectos.\n|- 9. Retomar proyecto\n|- 0. Salir\n|*******************************************")

def menu_funcional(tecla):
    
    lista_proyectos = cargar_csv_lista("Proyectos.csv")
    
    valor_ingresado = input()
    bandera = True
    
    while tecla != "0":
    
        match valor_ingresado:
                
            case "1":
                    
                proyecto = validar_agregar_proyecto()
                    
                print("Se agregó el siguiente proyecto: ")
                
                for key, value in proyecto.items():
                    
                    print(f"{key} - {value}")
                
                imprimir_menu()
                
                valor_ingresado = input()
                                    
            case "2":
                
                lista_proyectos = cargar_csv_lista("Proyectos.csv")
                    
                valor_ingresado = modificar_proyecto(lista_proyectos)

                imprimir_menu()
                
                valor_ingresado = input()
                    
            case "3":
                    
                cancelar_proyecto(lista_proyectos)

                imprimir_menu()
                
                valor_ingresado = input()
                                
            case "4":
                
                lista_proyectos = cargar_datos_fecha_fin('Proyectos.csv')
                
                lista_proyectos_actualizados = actualizar_estados(lista_proyectos)
                
                guardar_datos_fecha_fin('Proyectos.csv',lista_proyectos_actualizados)
                    
                print("Los proyectos fueron actulizados satisfactoriamente.")
                
                imprimir_menu()
                
                valor_ingresado = input()
                
            case "5":
                
                lista_proyectos = cargar_csv_lista("Proyectos.csv")
                    
                mostrar_todos(lista_proyectos)

                imprimir_menu()
                
                valor_ingresado = input()
                
            case "6":
                
                lista_csv = cargar_csv_lista('Proyectos.csv')
                     
                presupuesto_promedio = calcular_promedio(lista_csv, "Presupuesto")
                    
                print(f"El presupuesto promedio es de ${presupuesto_promedio}")
                
                imprimir_menu()
                
                valor_ingresado = input()   
                
            case "7":
                
                lista_proyectos = cargar_csv_lista('Proyectos.csv')
                    
                resultado = buscar_proyecto_por_nombre(lista_proyectos)
                    
                if resultado == "No hay ningún proyecto con ese nombre":
                        
                    print(resultado)
                    
                else:
                    for key, value in resultado.items():
                            
                        if key == "Presupuesto":
                                                        
                            print(f"{key} - ${value}")
                            
                        else: print(f"{key} - {value}")   
                
                imprimir_menu()
                
                valor_ingresado = input()
                
            case "8":
                
                lista_formateada = cargar_datos('Proyectos.csv')
                    
                ordenar_y_mostrar_proyectos(lista_formateada)
            
                imprimir_menu()
                
                valor_ingresado = input()
                        
            case "9":
                    
                dar_alta_proyecto_cancelado(lista_proyectos)
                
                imprimir_menu()
                
                valor_ingresado = input()
            
            case "10":
                
                presupuesto = input("Ingrese el presupuesto: ")
                
                validacion_entero =  validar_ingreso_numero_entero(presupuesto)
                
                while validacion_entero == True:
                    
                    presupuesto = input("Error, ingrese un numero entero.")
                    
                    validacion_entero =  validar_ingreso_numero_entero(presupuesto)
                
                lista_presupuesto = filtrar_proyectos_por_presupuesto(presupuesto)
                
                generar_reporte(lista_presupuesto)

            case "11":
                
                proyecto_nombre = input("Ingrese el nombre: ")
                
                lista_proyectos = cargar_csv_lista('Proyectos.csv')
                
                generar_reporte_por_nombre(lista_proyectos,proyecto_nombre)
                    
            case "0":
                
                print("Guarando archivos finalizados...")
                
                lista_proyectos = cargar_csv_lista('Proyectos.csv')

                proyectos_finalizados = []

                for i in lista_proyectos:
                    
                    if i['Estado'] == 'Finalizado':
                        
                        proyectos_finalizados.append(i)

                lista_id_proyectos_finalizados_json =  []

                json_finalizados = leer_json('ProyectosFinalizados.json')

                for i in json_finalizados['ProyectosFinalizados']:
                    
                    lista_id_proyectos_finalizados_json.append(i['id'])

                for i in proyectos_finalizados:
                    
                    if i['id'] not in lista_id_proyectos_finalizados_json:
    
                        escribir_json(i['id'], i['Nombre del Proyecto'], i['Descripcion'], i['Fecha de inicio'], i['Fecha de Fin'], i['Presupuesto'], i['Estado'])

                
                time.sleep(1.5)
                
                print("Archivos guardados correctamente...")
                
                time.sleep(1)
                
                input("Programa cerrado, pulse cualquier tecla para continuar.")
                tecla = "0"
                
            case "g":
                
                lista_proyectos = cargar_csv_lista('Proyectos.csv')
                
                lista_proyectos_inicados_en_invierno = proyectos_inicados_en_invierno(lista_proyectos)
                
                lista_presupuesto_maximo = obtener_presupuesto_mayor(lista_proyectos_inicados_en_invierno)
                
                for i in lista_presupuesto_maximo:
                
                    for key, value in i.items():
                        
                        print(f"{key} - {value}")
            
                imprimir_menu()
                
                valor_ingresado = input()
                
            case "s":
                
                lista_proyectos = cargar_csv_lista('Proyectos.csv')
                
                lista_proyectos_inactivos = obtener_proyectos_inactivos(lista_proyectos)
                
                lista_presupuesto_maximo = ordenar_por_presupuesto(lista_proyectos_inactivos)
                
                for i in lista_presupuesto_maximo:
                    
                    for key, valor in i.items():
                        
                        print(f"{key} - {valor}")
                
                imprimir_menu()
                
                valor_ingresado = input()
                                  
            case _:
                    
                asd = input("Ninguna es correcta")
                
                imprimir_menu()
                
                valor_ingresado = input()