def validar_formato_fechas(fecha):
    
    retorno = True
    
    partes = fecha.split('/')
    if len(partes) != 3:
        retorno =  False
    if not (partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit()):
        retorno = False
    if len(partes[0]) != 4 or len(partes[1]) != 2 or len(partes[2]) != 2:
        retorno = False
        
    return retorno

def convertir_fecha(fecha):
    
    partes = fecha.split("/")
    
    return datetime(int(partes[0]), int(partes[1]), int(partes[2]))

def fechas_validas(fecha1, fecha2):
    
    retorno = True
    
    if not (validar_formato_fechas(fecha1) and validar_formato_fechas(fecha2)):
        
        retorno = (False, "Formato de fecha incorrecto")
        
    fecha1 = convertir_fecha(fecha1)
    fecha2 = convertir_fecha(fecha2)
    
    if fecha1 >= fecha2:
        
        retorno = (False, "La fecha de fin es menor a al fecha inicio.")
    
    return retorno