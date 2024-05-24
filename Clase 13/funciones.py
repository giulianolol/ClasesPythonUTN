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
    
    pass

    #PAGINA 6 - FUNCION 4.1