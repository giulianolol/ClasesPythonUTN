import time, os

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
    
    valor_maximo = 0
    bandera = True
    
    for i in range(len(lista)):
        
        prueba = obtener_dato(lista[i], clave)
        
        if prueba == False:
            
            bandera = False
    
    if bandera != False:
        
        for x in lista:
            
            if type(x[clave]) == int or type(x[clave]) == float:
                
                for i in x:
                    
                    if x[clave] > valor_maximo:
                        
                        valor_maximo = x[clave]
    
    return valor_maximo

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
    valor_ingresado = input("1-A. Normalizar datos.\n2-B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB\n3-C. Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n4-D. Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n5-E. Recorrer la lista y determinar cuál es el superhéroe más débil de género M\n6-F. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB\n7-G. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\n8-H. Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n9-I. Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n10-J. Listar todos los superhéroes agrupados por color de ojos.\n11-K. Listar todos los superhéroes agrupados por tipo de inteligencia.\n")
    
    valor_validado = validar_entero(valor_ingresado)

    return valor_ingresado, valor_validado


def validar_entero(cadena:str):
    
    bandera_letra = False
    
    for i in range(len(cadena)):
        
        if not cadena[i].isdigit():
            
            bandera_letra = True
            
    return bandera_letra

def filtrar_datos_por_clave(lista:list, clave:str, valor_a_igualar, parametro:str):
    
    if parametro == "lista":
        
        lista_valores_igualados = []
        
        for i in lista:
            
            if i[clave] == valor_a_igualar:
                
                lista_valores_igualados.append(i["nombre"])
        
        retorno = lista_valores_igualados
        
    else:
        
        lista_diccionarios_igualados = []
        
        for i in lista:
            
            if i[clave] == valor_a_igualar:
                
                lista_diccionarios_igualados.append(i)
        
        retorno = lista_diccionarios_igualados

    return retorno

def stark_menu_principal():
    
    ingreso_usuario =  imprimir_menu()

    while ingreso_usuario[1] == True:

        print("Error. Ingrese un numero válido: ")
        ingreso_usuario =  imprimir_menu()

    ingreso_usuario = ingreso_usuario[0]

    ingreso_usuario = int(ingreso_usuario)

    return ingreso_usuario

def stark_marvel_app(lista):

    flag_datos_normalizados = False
    
    valor_ingresado = stark_menu_principal()

    while valor_ingresado != 1 and valor_ingresado != "1":

        valor_ingresado = input("Es necesario corregir los datos primero.\nIngrese el numero 1: ")

    stark_normalizar_datos(lista)
    flag_datos_normalizados =  True

    valor_ingresado = input("Datos normalizados correctamente. \nIngrese la funcion que desea utilizar: ")
    
    while valor_ingresado != 0 and valor_ingresado != "0":
    
        if valor_ingresado == 1 or valor_ingresado == "1":
            
            print("Los datos fueron noramlizados correctamente.")
            
            print("Cargando ...")
            time.sleep(3)
            os.system("cls")
            valor_ingresado = stark_menu_principal()

        elif flag_datos_normalizados == True and (valor_ingresado == "2" or valor_ingresado == 2):
            
            lista_heroes =  filtrar_datos_por_clave(lista,"genero","NB","lista")

            print("Superheroes de género NB:\n")
            
            for i in range(len(lista_heroes)):

                print(f"-{lista_heroes[i]}")
            
            print("\nCargando ...")
            time.sleep(3)
            os.system("cls")
                      
        elif flag_datos_normalizados == True and (valor_ingresado == "3" or valor_ingresado == 3):

            lista_heroes_F = filtrar_datos_por_clave(lista,"genero","F","diccionario")
            
            alutra_maxima_F = obtener_maximo(lista_heroes_F,"altura")
            
            lista_heroes_F_filtrada = obtener_dato_cantidad(lista_heroes_F,alutra_maxima_F,"altura")
            
            print("Superheroe/s mas alto de género F:\n")
            
            for i in range(len(lista_heroes_F_filtrada)):
                
                print(f"-{lista_heroes_F_filtrada[i]}")
            
            print("\nCargando...")
            time.sleep(3)
            os.system("cls")

        elif flag_datos_normalizados == True and (valor_ingresado == "4" or valor_ingresado == 4):

            lista_heroes_M = filtrar_datos_por_clave(lista,"genero","M","diccionario")
            
            alutra_maxima_M = obtener_maximo(lista_heroes_M,"altura")
            
            lista_heroes_F_filtrada = obtener_dato_cantidad(lista_heroes_M, alutra_maxima_M, "altura")
            
            print("Superheroe/s más alto de género M:\n")
            
            for i in range(len(lista_heroes_F_filtrada)):
                
                print(f"-{lista_heroes_F_filtrada[i]}")
            
            print("\nCargando...")
            time.sleep(3)
            os.system("cls")

        elif flag_datos_normalizados == True and valor_ingresado == "5" :

            pass

        elif flag_datos_normalizados == True and valor_ingresado == "6" :

            pass

        elif flag_datos_normalizados == True and valor_ingresado == "7" :

            pass

        elif flag_datos_normalizados == True and valor_ingresado == "8":

            pass

        elif flag_datos_normalizados == True and valor_ingresado == "9" :

            pass

        elif flag_datos_normalizados == True and valor_ingresado == "10" :

            pass

        elif flag_datos_normalizados == True and valor_ingresado == "11" :

            pass

        else:
            print("PASSAHRE")
             
        valor_ingresado = stark_menu_principal()