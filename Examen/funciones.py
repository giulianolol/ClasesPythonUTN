import csv
import time
from datetime import *

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
                
    
def leer_csv(nombre_archivo):
    
    datos = []
    
    with open(nombre_archivo, mode='r', newline='') as archivo_csv:
        
        lector_csv = csv.DictReader(archivo_csv)
        
        for fila in lector_csv:
            
            datos.append(dict(fila))
    
    return datos  

def escribir_csv(ruta_archivo, datos):
    
    file = open(ruta_archivo, 'a')
    
    file.writelines(datos)
        
    file.close()

def validar_ingreso_palabra(string):
    
    retorno = True
    
    for i in string:
        
        if i.isalpha() == False and i != " ":
            
            retorno = False
            break       
    
    return retorno

def validar_ingreso_numero_entero(numero:float):
    
    retorno = False
    
    if type(numero) != float:
    
        for i in numero:
            
            if i.isalpha() == True or i == "." or i ==",":
                
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

def validar_formato_fecha(cadena:str):
    
    contador = 0
    retorno = False
    
    for i in cadena:
        
        if i == "/": contador +=1
    
    if contador == 2: retorno = True
         
    return retorno

def validar_formato_fechas(fecha):
    
    retorno = True
    
    partes = fecha.split('/')
    if len(partes) != 3:
        retorno =  False
        
    elif not (partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit()):
        retorno = False
        
    elif len(partes[0]) != 2 or len(partes[1]) != 2 or len(partes[2]) != 4:
        retorno = False
        
    return retorno

def convertir_fecha(fecha):
    
    partes = fecha.split("/")
    
    dia = partes[0]
    mes = partes[1]
    anio = partes[2]
    
    retorno = datetime.datetime(dia,mes,anio)
    
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

def validar_agregar_proyecto():
    
    bandera_proyecto = False
    bandera_fecha = False
    
    datos = leer_csv('Proyectos.csv')

    nombre_proyecto = input("Ingrese el nombre del proyecto: ")
    
    validacion_nombre_proyecto = validar_ingreso_palabra(nombre_proyecto)
    
    while validacion_nombre_proyecto == False or len(nombre_proyecto) > 30:
        
        nombre_proyecto = input("Error, ingrese un nombre válido, menor a 30 caracteres: ")

        validacion_nombre_proyecto = validar_ingreso_palabra(nombre_proyecto)
    
    descripcion_proyecto = input("Ingrese la descripcion del proyecto: ")
    
    validacion_descripcion_proyecto = validar_ingreso_alfanumerico(descripcion_proyecto)
    
    while validacion_descripcion_proyecto == False or len(descripcion_proyecto) > 200:
        
        descripcion_proyecto = input("Error, debe ingresar una descripción válida. Solo caracteres alfanumeros y que no superen los 200 digitos.")
        
        validacion_descripcion_proyecto = validar_ingreso_alfanumerico(descripcion_proyecto)
    
    while bandera_proyecto == False:
        
        presupesto_proyecto = input("Ingrese el presupesto para el proyecto: ")
        
        validacion_presupuesto_proyecto = validar_ingreso_numero_entero(presupesto_proyecto)

        while validacion_presupuesto_proyecto == True:
            
            presupesto_proyecto = input("Error, debe ingresar un número entero: ")
            
            validacion_presupuesto_proyecto = validar_ingreso_numero_entero(presupesto_proyecto)
            
        presupesto_proyecto = int(presupesto_proyecto)
        
        if presupesto_proyecto < 500000:
            
            print("Error, ingrese un presupesto mayor a 500000: ")
            
            break
        
        bandera_proyecto = True
        
    
    while bandera_fecha == False:
        
        fecha_inicio = input("Ingrese la fecha de inicio del proyecto: ")
        """
        validacion_formato_fecha = validar_formato_fechas(fecha_inicio)
        
        while validacion_formato_fecha == False:
        
            fecha_inicio = input("Error, la fecha tiene que tener el siguiente formato. 'DD/MM/AAAA'")
        
            validacion_formato_fecha = validar_formato_fechas(fecha_inicio)
        
        fecha_inicio_formateada = convertir_fecha(fecha_inicio)
        """
        bandera_fecha = True
    
    bandera_fecha = False
    
    while bandera_fecha == False:
        
        fecha_fin = input("Ingrese la fecha de fin del proyecto: ")
        """
        validacion_formato_fecha = validar_formato_fechas(fecha_inicio)
        
        while validacion_formato_fecha == False:
            
            fecha_fin = input("Error, la fecha tiene que tener el siguiente formato. 'DD/MM/AAAA'")
            
            validacion_formato_fecha = validar_formato_fechas(fecha_fin)
        
        fecha_fin_formateada = convertir_fecha(fecha_fin)
        
        if fecha_fin_formateada < fecha_inicio_formateada:
            
            print("Error, la fecha de fin es anterior a la fecha de inicio.")
            
            break
        """    
        bandera_fecha = True
                                    
    estado_proyecto = input("Ingrese el estado del proyecto(Activo/Cancelado/Finalizado): ").capitalize()
    
    while estado_proyecto != "Activo" and estado_proyecto != "Cancelado" and estado_proyecto and "Finalizado":
        
        estado_proyecto = input("Error, el estado solo puede ser Activo, Cancelado o Finalizado.").capitalize()
    
    ultimo_id = int(datos[-1]['id']) if datos else 0
    
    proyecto = {'id':ultimo_id + 1,'Nombre del Proyecto':nombre_proyecto, 'Descripcion': descripcion_proyecto, 'Presupuesto':presupesto_proyecto,'Fecha de inicio': fecha_inicio, 'Fecha de Fin': fecha_fin, 'Estado': estado_proyecto}
    
    return proyecto
    

def modificar_proyecto(lista_proyectos:list):
    
    bandera_id_encontado = False
      
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
        
        imprimir_sub_menu(proyecto_diccionario)
    
    else: 
        
        print("Error, id no encontrado.")


def imprimir_sub_menu(proyecto_a_modificar:dict):
    
    print("Mostrando datos de proyecto acutual...")
    
    lista_posibles_valores = ["1", "2", "3", "4", "5", "6"]
    
    for key, value in proyecto_a_modificar.items():
            
        print(f"{key} - {value}")
    
    valor = input("*********************************************\n|- 1. Nombre del Proyecto.\n|- 2. Descripción.\n|- 3. Fecha de inicio.\n|- 4. Fecha de Fin.\n|- 5. Presupesto.\n|- 6. Estado.")
    
    validar_valor = validar_ingreso_numero_entero(valor)
    
    while validar_valor == True or valor not in lista_posibles_valores:    
            
        valor = input("Error, el valor ingresado no es válido. Tiene que ser un valor numérico y ser un valor entre el 1 y el 6.")
            
        validar_valor = validar_ingreso_numero_entero(valor)
    
    match valor:
        
        case "1":
            
            nombre_anterior =  proyecto_a_modificar["Nombre del Proyecto"]
            
            nombre_proyecto = input("Ingrese el nuevo nombre del proyecto: ")
    
            validacion_nombre_proyecto = validar_ingreso_palabra(nombre_proyecto)
    
            while validacion_nombre_proyecto == False or len(nombre_proyecto) > 30:
        
                nombre_proyecto = input("Error, ingrese un nombre válido, menor a 30 caracteres: ")

                validacion_nombre_proyecto = validar_ingreso_palabra(nombre_proyecto)
            
            proyecto_a_modificar["Nombre del Proyecto"] = nombre_proyecto
            
            print(f"El nombre se modificó correctamente.\n|- Nombre anterior: {nombre_anterior}\n|- Nombre actualizado: {proyecto_a_modificar['Nombre del Proyecto']}")
            
            tecla = input("Ingrese una tecla para continuar.")
        
        case "2":
            
            descripcion_anterior = proyecto_a_modificar["Descripcion"]
            
            descripcion_proyecto = input("Ingrese la nueva descripcón del proyecto: ")
            
            validacion_descripcion_proyecto = validar_ingreso_alfanumerico(descripcion_proyecto)
    
            while validacion_descripcion_proyecto == False or len(descripcion_proyecto) > 200:
        
                descripcion_proyecto = input("Error, debe ingresar una descripción válida. Solo caracteres alfanumeros y que no superen los 200 digitos.")
        
                validacion_descripcion_proyecto = validar_ingreso_alfanumerico(descripcion_proyecto)
            
            proyecto_a_modificar["Descripcion"] = descripcion_proyecto
            
            print(f"La descripcion se modificó correctamente.\n|- Descripcion anterior: {descripcion_anterior}\n|- Descripcion actualizada: {proyecto_a_modificar['Descripcion']}")
                         
            tecla = input("Ingrese una tecla para continuar.")        
            
        case "3":
            
           pass 
        
        case "4":
            
            pass
        
        case "5":
            
            bandera_proyecto = False
            presupuesto_anterior = proyecto_a_modificar["Presupuesto"]
            
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
            
            print(f"El presupuesto se modificó correctamente.\n|- Presupuesto anterior: {presupuesto_anterior}\n|- Precupesto actualizado: {proyecto_a_modificar['Presupuesto']}")       
                    
            tecla = input("Ingrese una tecla para continuar.")
        
        case "6":
            
            estado_anterior = proyecto_a_modificar["Estado"]
            
            estado_proyecto = input("Ingrese el nuevo estado del proyecto: ")
            
            while estado_proyecto != "Activo" and estado_proyecto != "Cancelado" and estado_proyecto and "Finalizado":
        
                estado_proyecto = input("Error, el estado solo puede ser Activo, Cancelado o Finalizado.").capitalize()
            
            print(f"El estado se modificó correctamente.\n|- Estado anterior: {estado_anterior}\n|- Estado actualizado: {proyecto_a_modificar['Estado']}")
                    
            tecla = input("Ingrese una tecla para continuar.")
            
def cancelar_proyecto(lista_proyectos):
    
    datos =  leer_csv('Proyectos.csv')
    
    bandera_id_encontado = False
      
    id = input("Ingrese el id del proyecto a cancelar: ")
        
    validacion_id = validar_ingreso_numero_entero(id)
        
    while validacion_id == True:
            
        id = input("Error, ingres un valor numérico.")
            
        validacion_id = validar_ingreso_numero_entero(id)
        
    for i in range(len(lista_proyectos)):
        
        if lista_proyectos[i]["id"] == id:
            
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
        presupuesto = f"${float(proyecto['Presupuesto']):,.2f}"
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
  
def imprimir_menu():

    print("*********************************************\n|- 1. Ingresar proyecto.\n|- 2. Modificar proyecto.\n|- 3. Cancelar proyecto.\n|- 4. Comprobar proyectos.\n|- 5. Mostrar todos.\n|- 6. Calcular presupuesto promedio.\n|- 7. Buscar proyecto por nombre.\n|- 8. Ordenar proyectos.\n|- 9. Retomar proyecto\n|- 10. Salir\n|*******************************************")


def menu_funcional():
    
    
    lista_proyectos = leer_csv("Proyectos.csv")
    valor_ingresado = input()
    bandera = True
    
    while bandera == True:
    
        match valor_ingresado:
            
            case "1":
                
                proyecto = validar_agregar_proyecto()
                
                print(proyecto)
                
                break
                
            case "2":
                
                valor_ingresado = modificar_proyecto(lista_proyectos)
                
                break
                
            case "3":
                
                cancelar_proyecto(lista_proyectos)
                
                break
                            
            case "4":
                
                prueba = "as"
                asd = input("Comprobar proyectos")
                break
            
            case "5":
                
                mostrar_todos(lista_proyectos)
                break
            
            case "6":
                
                presupuesto_promedio = calcular_promedio(lista_proyectos, "Presupuesto")
                
                print(f"El presupuesto promedio es de ${presupuesto_promedio}")
                
                break
            
            case "7":
                
                prueba = "as"
                asd = input("Buscar proyecto por nombre")
                break
                
            case "8":
                
                prueba = "asd"
                asd = input("Ordernar proyecto")
                break
                
            case "9":
                
                prueba = 32
                asd = input("Retornar proyecto")
                break
                
            case "10":
                
                prueba = "oeoe"
                asd = input("Salir")
                bandera = False
                break
                                        
            case _:
                
                prueba = "ddf"
                asd = input("Ninguna es correcta")
                break


menu_funcional()
