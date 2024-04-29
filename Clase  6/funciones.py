def sumar_ingresos(lista:list):
    
    suma = 0
    
    for i in range(len(lista)):

        suma += lista[i]
        
    return suma

def calcular_dia_mayor_ingreso(dias_semana):
    
    bandera = False
    
    for i in range(0,6):
        
        ingresos_dia = sumar_ingresos(dias_semana[i])
        
        if bandera == False:
        
            mayor_ingreso = ingresos_dia
            dia_mayor_ingreso = dias_semana[i+1]
            bandera = True
        
        if ingresos_dia > mayor_ingreso:
            
            mayor_ingreso = ingresos_dia
            dia_mayor_ingreso = dias_semana[i+1]
    
    return dia_mayor_ingreso

def calcular_dia_menor_ingreso(dias_semana):
    
    bandera = False
    
    for i in range(0,6):
        
        ingresos_dia = sumar_ingresos(dias_semana[i])
        
        if bandera == False:
        
            menor_ingreso = ingresos_dia
            dia_menor_ingreso = dias_semana[i+1]
            bandera = True
        
        if ingresos_dia < menor_ingreso:
            
            menor_ingreso = ingresos_dia
            dia_menor_ingreso = dias_semana[i+1]
    
    return dia_menor_ingreso

def calcular_promedio(dias_semana):
    
    suma_total = 0
    
    for i in range(len(dias_semana)):
        
        ingresos_dia = sumar_ingresos(dias_semana[i])
        
        suma_total += ingresos_dia
    
    promedio = suma_total / 6
    
    return promedio

def calcular_suma_semana(dias_semana):
    
    suma_total = 0
    
    for i in range(len(dias_semana)):
        
        suma_total += sumar_ingresos(dias_semana[i])
        
    return suma_total

def promedio_dias(dias_semana,dia_principio, dia_final):
    
    suma_promedio = 0
    
    for i in range(dia_principio,dia_final):
        
        promedio = calcular_promedio(dias_semana[i])
        
        suma_promedio += promedio
    
    return suma_promedio

def promedio_dia_semana(dias_semana):
    
    suma_finde = 0
    suma_semana = 0
    bandera_finde = False
    
    for i in range(0,7):
        
        if i >= 5:          
            suma_finde += sumar_ingresos(dias_semana[i])
            bandera_finde = True
        else:
            suma_semana += sumar_ingresos(dias_semana[i])
    
    if bandera_finde == True:
    
        promedio_fin_semana = suma_finde / 2
        
        retorno = promedio_fin_semana
    
    else:
        
        promedio_semana = suma_semana / 5
        
        retorno = promedio_semana
        
    return retorno

def dia_mayor_variacion(dia_de_la_semana:list):
    
    mayor_variacion = 0
    
    dia_mayor_variacion = 0
    
    for i in range(1,len(dia_de_la_semana)):
        
        variacion = dia_de_la_semana[i] - dia_de_la_semana[i-1]
        
        if variacion > mayor_variacion:
            
            mayor_variacion = variacion
            dia_mayor_variacion = i
    
    return dia_mayor_variacion

def numero_pasado_a_dia(x):
    if x == 0:       
        dia = "Lunes"
    elif x == 1:     
        dia = "Martes"
    elif x == 2:  
        dia = "Miercoles"
    elif x == 3:
        dia = "Jueves"
    elif x == 4:
        dia = "Viernes"
    elif x == 5:
        dia = "Sabado"
    elif x == 6:
        dia = "Domingo"
    
    return dia


suma_total_semana = []

dias_semana = []

lunes = [1]
martes = [2]
miercoles = [9]
jueves = [4]
viernes = [5]
sabado = [6]
domingo =[0]

dias_semana.append(lunes)
dias_semana.append(martes)
dias_semana.append(miercoles)
dias_semana.append(jueves)
dias_semana.append(viernes)
dias_semana.append(sabado)
dias_semana.append(domingo)

print(dias_semana)

letra_ingresada = input("¡Bienvenido! Ingrese la opción que desea ejecutar.\nA) Registrar un ingreso en la lista de ingresos mensuales.\nB) Analizar y calcular los datos.\nC) Cerrar el programa.")
    
    
letra_ingresada = letra_ingresada.lower()
    
while letra_ingresada != "c" and letra_ingresada != "b" and letra_ingresada !="a":
    letra_ingresada = input("Caracter no valido!.")
        
if letra_ingresada == "a":
        
    dia_hoy = input("Ingrese el dia de hoy de acuerdo a su numero.\n1.Lunes\n2.Martes\n3.Miercoles\n4.Jueves\n5.Viernes\n6.Sábado\n7.Domingo")
        
    while dia_hoy != "1" and dia_hoy != "2" and dia_hoy != "3" and dia_hoy != "4" and dia_hoy != "5" and dia_hoy != "6" and dia_hoy != "7":
            
        dia_hoy = input("Numero no valido!.")
        
    dia_hoy = int(dia_hoy)
        
    ingreso = input("Ingrese el monto.")
        
    while ingreso.isalpha(): #Entiendo que no se pueden usar metodos, para hacer la algoritmia haría un for que recorra una lista con todo el abecedario y retornaria que no es valido si en algun punto el ingreso coincide. Pero el isalpha es mas rápido.
            
        ingreso = input("Monto no valido!")
    
    ingreso = float(ingreso)    
    dia_hoy = dia_hoy - 1
    
    for i in range(len(dias_semana)):
        
        if i == dia_hoy:
            
            dias_semana[i].append(ingreso)
            
            print("Ingreso agregado correctamente.")
            
            agregar_a_lista_total = input("¿Desea agregarlo a la lista de sumas totales de la semana? 1.Si - 2.No")
            
            while agregar_a_lista_total.isalpha(): #Entiendo que no se pueden usar metodos, para hacer la algoritmia haría un for que recorra una lista con todo el abecedario y retornaria que no es valido si en algun punto el ingreso coincide. Pero el isalpha es mas rápido.
                
                agregar_a_lista_total = input("Valor no valido!")
            
            agregar_a_lista_total = int(agregar_a_lista_total)

            if agregar_a_lista_total == 1:
                
                suma_total_semana.append(ingreso)
    
if letra_ingresada == "b":
    
    dia_mayor_ingreso = calcular_dia_mayor_ingreso(dias_semana)
    dia_mayor_ingreso = numero_pasado_a_dia(dia_mayor_ingreso[0])
    
    dia_menor_ingreso = calcular_dia_menor_ingreso(dias_semana)
    dia_menor_ingreso = numero_pasado_a_dia(dia_menor_ingreso[0])
    
    promedio = calcular_promedio(dias_semana)
    ingreso_suma_semana = calcular_suma_semana(dias_semana)
    promedio_semana = promedio_dia_semana(dias_semana)
    promedio_fin_semana = promedio_dia_semana(dias_semana)
    
    for i in range (1,len(dias_semana)):
        dia_variacion_maxima = dia_mayor_variacion(dias_semana[i])  
    
    dia_variacion_maxima = numero_pasado_a_dia(dia_variacion_maxima)
    
    
    print(f"El dia con mayor ingresos fue el dia {dia_mayor_ingreso}, el dia con menor ingresos fue {dia_menor_ingreso}, El promedio de ingresos de la semana fue {promedio},el total de ingresos en la semana fue {ingreso_suma_semana},el promedio de ingresos de lunes a viernes fue {promedio_semana},el promedio de ingresos el sábado y el domingo fue {promedio_fin_semana},el dia de mas variacion respecto al dia anterior fue{dia_variacion_maxima}. ")
    print(f"{dias_semana[6]}")