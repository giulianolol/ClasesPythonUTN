import csv
from datetime import *



def contar_proyectos_activos(lista: list):

    contador = 0
    
    for i in range(len(lista)):
        
        if lista[i]["Estado"] == "Activo":
            
            contador +=1

            if contador == 50:
                
                print("Ya llegaste al límite de 50 proyectos activos, elimina alguno para contiunar.")
                break
    
    if contador < 50:
        
        print("Todo ok")
                
    
def leer_csv(nombre_archivo):
    
    datos = []
    
    with open(nombre_archivo, 'r', newline='') as archivo_csv:
        
        lector_csv = csv.DictReader(archivo_csv)
        
        for fila in lector_csv:
            
            datos.append(dict(fila))
    
    return datos  

def escribir_csv(datos):
    
    with open('Proyectos.csv', mode ='r', newline ='', encoding='utf-8') as file:
        
        lector_csv = csv.DictReader(file)
        encabezados = lector_csv.fieldnames
    
    with open('Proyectos.csv', mode='a', newline='') as archivo:
        
        escritor_csv = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor_csv.writerows(datos)

def validar_ingreso_palabra(string):
    
    retorno = True
    
    for i in string:
        
        if i.isalpha() == False:
            
            retorno = False
            break       
    
    return retorno

def validar_ingreso_numero(numero:float):
    
    retorno = False
    
    for i in numero:
        
        if i.isalpha() == True:
            
            retorno = True
            break
    
    return retorno
         
def validar_ingreso_alfanumerico(string:str):
    
    retorno = True
    
    for i in string:
        
        if i.isalnum() == False:
            
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
        
        validacion_presupuesto_proyecto = validar_ingreso_numero(presupesto_proyecto)

        while validacion_presupuesto_proyecto == True:
            
            presupesto_proyecto = input("Error, debe ingresar un número: ")
            
            validacion_presupuesto_proyecto = validar_ingreso_numero(presupesto_proyecto)
            
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
    
             
        
def imprimir_menu():

    print("*********************************************\n|- 1. Ingrear proyecto.\n|- 2. Modificar proyecto.\n|- 3. Cancelar proyecto.\n|- 4. Comprobar proyectos.\n|- 5. Mostrar todos.\n|- 6. Calcular presupuesto promedio.\n|- 7. Buscar proyecto por nombre.\n|- 8. Ordenar proyectos.\n|- 9. Retomar proyecto\n|- 10. Salir\n|*******************************************")


def menu_funcional():
    
    valor_ingresado = input()
    bandera = True
    
    while bandera == True:
    
        match valor_ingresado:
            
            case "1":
                
                prueba = "as"
                asd = input("Ingresar proyecto")
                break
                
            case "2":
                
                prueba = "asd"
                asd = input("Modificar proyecto")
                break
                
            case "3":
                
                prueba = 32
                asd = input("Cancelar proyecto")
                break
                            
            case "4":
                
                prueba = "as"
                asd = input("Comprobar proyectos")
                break
            
            case "5":
                
                prueba = "asd"
                asd = input("Mostrar todos")
                break
            
            case "6":
                
                prueba = 32
                asd = input("Calcular presupesto promedio")
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