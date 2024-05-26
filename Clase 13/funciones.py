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
    valor_ingrsado = input("A. Normalizar datos.\nB. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB\nC. Recorrer la lista y determinar cuál es el superhéroe más alto de género F\nD. Recorrer la lista y determinar cuál es el superhéroe más alto de género M\nE. Recorrer la lista y determinar cuál es el superhéroe más débil de género M\nF. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB\nG. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\nH. Determinar cuántos superhéroes tienen cada tipo de color de ojos.\nI. Determinar cuántos superhéroes tienen cada tipo de color de pelo.\nJ. Listar todos los superhéroes agrupados por color de ojos.\nK. Listar todos los superhéroes agrupados por tipo de inteligencia.")
    
    return valor_ingrsado


def validar_entero(cadena:str):
    
    bandera_no_digito = True
    
    for i in range(len(cadena)):
        
        if cadena[i].isdigit() == False:
            
            bandera_no_digito = False
            
    return bandera_no_digito

def stark_menu_principal():
    
    pass