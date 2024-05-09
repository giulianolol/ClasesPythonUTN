import datetime

def registrar_mascota(lista_mascotas):
    
    lista_aux = []
    
    dni_dueño = input("Ingrese DNI del dueño de la mascota: ")
    nombre_mascota = input("Ingrese el nombre de la mascota:  ")
    edad = int(input("Ingrese la edad de la mascota: "))
    especie = input("Ingrese la especie de la mascota: ").lower()
    sexo_mascota = input("Ingrese el sexo de la mascota.\n-Masculino(M).\n-Femenino(F). ").lower()
    peso_mascota = float(input("Ingrese el peso de la mascota: "))
    fecha_ultima_visita = input("Ingrese la fecha de su ultima visita: ")
    fecha_ultima_visita = fecha_ultima_visita.strftime("%d-%m-%Y")
    historial_medico = input("Ingrese Historial Medico:  ")
    
    lista_aux.append(dni_dueño)
    lista_aux.append(nombre_mascota)
    lista_aux.append(edad)
    lista_aux.append(especie)
    lista_aux.append(peso_mascota)
    lista_aux.append(sexo_mascota)
    lista_aux.append(peso_mascota)
    lista_aux.append(fecha_ultima_visita)
    lista_aux.append(historial_medico)
    
    lista_mascotas.append(lista_aux)
    
    print("Mascota registrada satisfactoriamente...")

def dar_consulta_medica(lista_mascotas):
    
    print("Ingres el numero correspondiente a la mascota de la cual quiere dar una consulta medica.")
    
    for i in range(len(lista_mascotas)):
        
        print(f"{i+1}.{lista_mascotas[i][1]}")
        
    nro_mascota = int(input("")) - 1
    
    lista_mascotas[nro_mascota][7] = input("Ingrese la consulta medica: ")
    
    print(f"Consulta medica de: {lista_mascotas[nro_mascota][1]}, actualizada: {lista_mascotas[nro_mascota][7]}")

def mostrar_todas_las_mascotas(lista_mascotas):
    
    print("Mostrando todas las mascotas: ")
    
    for i in range(len(lista_mascotas)):
        
        print(f"{lista_mascotas[i][1]}")

def calcular_promedio(lista, x):
    
    suma = 0
    
    for i in range(len(lista)):
        
        suma += lista[i][x]
    
    promedio = suma / len(lista)
    
    return promedio
    
def mostrar_mascotas_que_superan_promedio_edad(lista_mascotas):
    
    promedio_edad = calcular_promedio(lista_mascotas,2)
    lista_mascotas_promedio_mayor = []
    
    for i in range(len(lista_mascotas)):
        
       if lista_mascotas[i][2] > promedio_edad:
           
           lista_mascotas_promedio_mayor.append(lista_mascotas[i][1])
    
    for i in range(len(lista_mascotas_promedio_mayor)):
        
        print (f"Las cantidad de mascotas con una edad mayor al promedio son{lista_mascotas_promedio_mayor[i]}")

def calcular_promedio_mascotas(lista_mascotas):
    
    promedio_mascotas = calcular_promedio(lista_mascotas, 1)
    
    print(f"El promedio de mascotas es: {promedio_mascotas}")

def calcular_cantida_perros(lista_mascotas):
    
    contador = 0
    
    for i in range(len(lista_mascotas)):
        
        if lista_mascotas[i][3] == "perro":
            
            contador += 1
    
    print(f"La cantidad de perros es: {contador}")

def identificar_tipo_de_mascota_mas_registrada(lista_mascotas):
    
    cantidad_por_especie = {}
    
    for datos in lista_mascotas:
        
        especie = datos[3]
        
        if especie in cantidad_por_especie:
            
            cantidad_por_especie[especie] +=1
        
        else:
            
            cantidad_por_especie[especie] = 1
            
    for especie, cantidad in cantidad_por_especie.items():
        
        print(f"Hay {cantidad} animales de la especie {especie}")
                