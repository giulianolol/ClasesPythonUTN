def calcular_promedio(lista_numeros:list):
    
    suma = 0
    
    for i in lista_numeros:
        
        suma += i
        
    promedio = suma / len(lista_numeros)
    
    return promedio

def calcular_promedio_positivos(lista_numeros:list):
    
    suma_numeros_pos = 0
    acumulador = 0
    
    for i in range(len(lista_numeros)):
        
        if lista_numeros[i] >= 0:
            acumulador += 1
            suma_numeros_pos += lista_numeros[i]
        
                   
    promedio_positivos = suma_numeros_pos / acumulador
    
    return promedio_positivos

def calcular_producto(lista_numeros:list):
     
    acumulador = 1
     
    for i in range(len(lista_numeros)):
        
        acumulador *= lista_numeros[i]

    return acumulador

def posicion_maximo(lista_numeros:list):
    
    lista_pos = []
    flag_primera_vuelta = False
    
    for i in range(len(lista_numeros)):
        
        if flag_primera_vuelta == True:
            mayor = lista_numeros[i]
            flag_primera_vuelta = False
            
        if (i == 0 or mayor < lista_numeros[i]):
            
            lista_pos.clear()
            lista_pos.append(i)
            
        elif(lista_numeros[i] == mayor):
            
            lista_pos.append(i)
    
    return lista_pos

def reemplazar_nombres(lista_nombres:list, nombre_a_reemplazar, nombre_reemplazo):
    
    reemplazos_realizados = 0
    
    for i in range(len(lista_nombres)):
        
        if lista_nombres[i] == nombre_a_reemplazar:
            
            lista_nombres[i] = nombre_reemplazo
            
            reemplazos_realizados += 1

    return reemplazos_realizados