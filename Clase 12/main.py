#def contar_palabras(cadena: str):  
    string = cadena.split(".")
    return len(string)

#def devolver_cada_palabara_mayusc(cadena: str):

    lista = cadena.split(" ")
    string_axu = ""
    
    for i in range(len(lista)):
        
        palabra_aux = lista[i].capitalize()
    
        string_axu += f"{palabra_aux}\n"
    
    return string_axu

#def cadena_tercera_palabra_inpar(cadena: str):
    
    lista = cadena.strip('')
    cadena_aux = ""
    
    for i in range(len(lista)):
        
        if i % 2 != 0:
            
            lista[i].replace(new="")
        
        cadena_aux += f" {i}"
    
    return cadena_aux

#def cadena_posicion_par_mayusc(cadena: str):
    
    cadena_aux =""
    
    for i in cadena:
        
        if i % 2 == 0:
            
            cadena_aux += i.upper()
    
    return cadena_aux

#def cadena_mas_larga(cadena: str):
    
    lista = cadena.split(" ")
    longitud_palabra_mayor = 0
    flag_palabra = False
        
    for i in lista:
        
        if flag_palabra == False:
            
            longitud_palabra_mayor = len(i)
            palabra_mayor = i
            flag_palabra = True
        
        elif len(i) > longitud_palabra_mayor:
            
            palabra_mayor = i
    
    return palabra_mayor

#def funcion_validacion_enteros(cadena: str):
    
    for i in cadena:
        
        if not i.isdigit():
            
            msg = "Datos no validos"
    
    msg = "Datos validados"
    
    return msg

#def ordenar_palabras(cadena: str):
    
    lista = cadena.split(" ")
    string_axu = ""
    
    for i in range(len(lista)):
        
        palabra_aux = lista[i].capitalize()
    
        string_axu += f"{palabra_aux}\n"
    
    return string_axu


def contar_palabras(cadena: str):