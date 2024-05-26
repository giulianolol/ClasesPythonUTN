import time

def stark_normalizar_datos(lista):

    bandera_dato_modificado = False

    if bandera_dato_modificado == False and len(lista) > 0:

        for x in lista:

            if "fuerza" in x and type(x["fuerza"]) != int:

                x["fuerza"] = int(x["fuerza"])
                    
                bandera_dato_modificado = True
                
            if "altura" in x and type(x["altura"]) != float:

                x["altura"] = float(x["altura"])

                bandera_dato_modificado = True

            if "peso" in x and type(x["peso"]) != float:

                x["peso"] = float(x["peso"])

                bandera_dato_modificado = True

        retorno = True

    else: retorno = False


    return retorno

def obtener_dato(diccionario:dict, clave:str):
    
    if len(diccionario) > 0 and clave in diccionario:
        
        retorno = True
    
    else: retorno = False
    
    return retorno

def obtener_nombre(diccionario:dict, clave:str):
    
    prueba = obtener_dato(diccionario, clave)
    
    if prueba != False:
        
        retorno = f"Nombre: {diccionario['nombre']}"
        
    else: retorno = False
    
    return retorno
        
def obtener_nombre_y_dato(diccionario:dict, clave:str):
    
    prueba = obtener_nombre(diccionario, clave)
    
    if prueba != False:
        
        msg = f"Nombre: {diccionario['nombre']} | {clave}: {diccionario[clave]}"
        
    else: msg = False
    
    return msg

def obtener_maximo(lista:list, clave:str):
    
    valor_minimo = 0
    bandera = True
    
    for i in range(len(lista)):
        
        prueba = obtener_dato(lista[i], clave)
        
        if prueba == False:
            
            bandera = False
    
    if bandera != False:
        
        for i in range(len(lista)):
            
            if type(lista[i][clave]) == int or type(lista[i][clave]) == float:
                
                for i in range(len(lista[i])):
                    
                    if lista[i][clave] > valor_minimo:
                        
                        valor_minimo = lista[i][clave]
    
    return valor_minimo

def obtener_minimo(lista: list, clave: str):
    
    valor_minimo = 0
    bandera = True
    
    for i in range(len(lista)):
        
        prueba = obtener_dato(lista[i], clave)
        
        if prueba == False:
            
            bandera = False
    
    if bandera != False:
        
        for i in range(len(lista)):
            
            if type(lista[i][clave]) == int or type(lista[i][clave]) == float:
                
                for i in range(len(lista[i])):
                    
                    if bandera == True:
                        
                        valor_minimo = lista[i][clave]
                        bandera = False
                    
                    else:
                    
                        if lista[i][clave] < valor_minimo:
                            
                            valor_minimo = lista[i][clave]
    
    return valor_minimo

def obtener_dato_cantidad(lista:list, num:int, clave:str):
    
    lista_heroes = []
    
    bandera = True
    
    for i in range(len(lista)):
        
        prueba = obtener_dato(lista[i], clave)
        
        if prueba == False:
            
            bandera = False
    
    if bandera == True:
    
        for i in range(len(lista)):
            
            if lista[i][clave] == num:
                
                lista_heroes.append(lista[i]["nombre"])
    
    return lista_heroes

def stark_imprimir_heroes(lista:list):
    
    if not lista:
        
        retorno = False
        
    for i in range(len(lista)):
        
        print(lista[i])
        
def sumar_dato_heroe(lista:list, clave:str):
    
    suma = 0
    
    for i in range(len(lista)):
        
        if type(lista[i]) == dict and len(lista[i]) > 0:
            
            if clave == "fuerza" or clave == "altura" or clave == "peso":
                
                suma += lista[i][clave]
        
    return suma

def dividir(diviendo: int, divisor:int):
    
    if divisor != 0:
    
        retorno = diviendo / divisor
        
    else: retorno = False
    
    return retorno

def calcular_promedio(lista:list, clave:str):
    
    suma_dato = sumar_dato_heroe(lista, clave)
    
    promedio = dividir(suma_dato, len(lista))
    
    return promedio

def mostrar_promedio_dato(lista:list, clave:str):
    
    if lista:
    
        for i in range(len(lista)):
            
            if type(lista[i]) != int and type(lista[i]) != float:
                
                retorno = False
            
            else:
                
                retorno = True
    
    else: retorno = False
    
    return retorno

def imprimir_menu():
    valor_ingresado = input("1-A. Normalizar datos.\n2-B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB\n3-C. Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n4-D. Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n5-E. Recorrer la lista y determinar cuál es el superhéroe más débil de género M\n6-F. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB\n7-G. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\n8-H. Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n9-I. Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n10-J. Listar todos los superhéroes agrupados por color de ojos.\n11-K. Listar todos los superhéroes agrupados por tipo de inteligencia.")
    
    valor_validado = validar_entero(valor_ingresado)

    return valor_ingresado, valor_validado

def validar_entero(cadena:str):
    
    bandera_letra = False
    
    for i in range(len(cadena)):
        
        if not cadena[i].isdigit():
            
            bandera_letra = True
            
    return bandera_letra

def stark_menu_principal():
    
    ingreso_usuario =  imprimir_menu()

    while ingreso_usuario[1] == True:

        print("Error. Ingrese un numero válido.")
        print("Cargando...")
        time.sleep(2)
        ingreso_usuario =  imprimir_menu()

    ingreso_usuario = ingreso_usuario[0]

    ingreso_usuario = int(ingreso_usuario)

    return ingreso_usuario

def stark_marvel_app(lista):

    bandera_datos_corregidos = False

    valor_ingresado = stark_menu_principal()

    if valor_ingresado == 1:

        print("Datos corregidos satisfactoriamente.")
        bandera_datos_corregidos = True
    
    elif valor_ingresado == 2 and bandera_datos_corregidos == True:

        pass

    elif valor_ingresado == 3 and bandera_datos_corregidos == True:

        pass

    elif valor_ingresado == 4 and bandera_datos_corregidos == True:

        pass

    elif valor_ingresado == 5 and bandera_datos_corregidos == True:

        pass

    elif valor_ingresado == 6 and bandera_datos_corregidos == True:

        pass

    elif valor_ingresado == 7 and bandera_datos_corregidos == True:

        pass

    elif valor_ingresado == 8 and bandera_datos_corregidos == True:

        pass

    elif valor_ingresado == 9 and bandera_datos_corregidos == True:

        pass

    elif valor_ingresado == 10 and bandera_datos_corregidos == True:

        pass

    elif valor_ingresado == 11 and bandera_datos_corregidos == True:

        pass