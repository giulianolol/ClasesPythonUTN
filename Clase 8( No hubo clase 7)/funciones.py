def calcular_promedio(x,y):
    
    resultado =  x / y
    
    return resultado 

def calcular_alumnos_condicion(lista):
    
    sumar_notas = 0
    
    for i in range(len(lista)):
        
        sumar_notas += sumar_nota(lista[i],"promocion")
    
    return sumar_notas
    
def sumar_nota(lista,condicion):
    
    contador = 0
    

        
    if condicion == "promocion":
            
        if i >= 6:
                
            contador +=1
            
    elif condicion == "aprobado":
            
        if i >= 4:
                
            contador +=1
            
    elif condicion == "desparobado":
            
        if i < 4:
                
            contador +=1
        
        else:
            
            return "Condicion Invalida"
    
    return contador

def calcular_notas_masculinos(edad,genero):
    
    nota = 0
    
    for i in range(len(edad)):
    
        if genero[i] == "g":
            
            nota += edad[i]

    return nota

def calcular_alumnas_sobre_total(total_alumnas, notas):
    
    suma_notas = sumar_nota(total_alumnas,"promocion")
    
    resultado = suma_notas / total_alumnas * 100
    
    return resultado
        
    

def sumar_edades(lista):
    
    suma = 0
    
    for i in range(len(lista)):
        
        suma += lista[1]
    
    return suma


lista_alumnos = [["L",20,123,"m",9],["L",10,123,"m",9],["L",20,123,"f",9],["L",10,123,"f",9]]
"""
for i in range(2):
    
    lista_aux = []
    
    nombre = input("Ingrese Nombre: ")
    edad = int(input("Ingrese Edad: "))
    
    
    dni = input("Ingrese Dni: ")
    genero = input("Ingrese genero: \n-Masculino(M)\n-Femenino(F)\n-Otro(X): ").lower() 
    
    nota = int(input("Ingrese Nota: "))
    
    lista_aux.append(nombre)
    lista_aux.append(edad)
    lista_aux.append(dni)
    lista_aux.append(genero)
    lista_aux.append(nota)
    
    lista_alumnos.append(lista_aux)
"""

suma_edades = sumar_edades(lista_alumnos[1])
    
promedio_edades = calcular_promedio(suma_edades,len(lista_alumnos[0]))

alummnos_promocionados = 0

for i in range(len(lista_alumnos)) :
    
    resultado = sumar_nota(lista_alumnos[i][4],"promocion")
    
    alummnos_promocionados += resultado

alumnos_aprobados = 0

for i in range(len(lista_alumnos)):
    
    resultado = calcular_alumnos_condicion(lista_alumnos[i])

    alumnos_aprobados += resultado

alumnos_desaprobados = 0

for i in range(len(lista_alumnos)):
    
    resultado = calcular_alumnos_condicion(lista_alumnos[i])
    
    alumnos_desaprobados += resultado

promedio_notas_masculinos = calcular_notas_masculinos(lista_alumnos[4],lista_alumnos[3])

alumnas_femeninas = 0

for i in range(len(lista_alumnos[3])):
    
    if lista_alumnos[3][i] == "m":
        
        alumnas_femeninas += 1

porcentaje_alumnas_sobre_total = calcular_alumnas_sobre_total(alumnas_femeninas,lista_alumnos[4])

print(f"Promedio edades {promedio_edades}, alumnos promocionados {alumnos_promocionados}, alumnos aprobados {alumnos_aprobados}, alumnos desaprobados {alumnos_desaprobados}, alumnos, promedio edades masculinos{promedio_notas_masculinos}, porcenaje alumnas promoconadas sobre el total {porcentaje_alumnas_sobre_total}")