"""
1.Crear una función que reciba como parámetro una cadena y determine
cuántas lista[x]s contiene. La función deberá retornar un entero indicando el
número de lista[x]s.
2. Crear una función que reciba como parámetro una cadena y devuelva la
misma cadena pero con cada lista[x] empezando con una letra mayúscula.
Ej: Si recibe como parámetro la cadena "hola mundo" debe devolver "Hola
Mundo".
3. Crear una función que reciba una cadena y devuelva una nueva cadena donde
todas las lista[x]s de posición impar sean eliminadas.
Ej: Si recibe la cadena "Este es un ejemplo" debe devolver "Este un".
4. Crear una función que reciba una cadena y devuelva esa misma cadena pero
con todas las letras en posición par en mayúsculas.
Ej: Si recibe la cadena “ejemplo”, debe devolver “eJeMpLo”
5. Crear una función que reciba una cadena y devuelva la lista[x] más larga de
la misma.
Ej: Si recibe “Esta es una frase de ejemplo”, debe de retornar “ejemplo”
6. Crear una función que pida un número entero, validando que no se ingresen
otro tipo de caracteres
7. Crear una función que reciba una cadena y la devuelva de manera ordenada y
con las mayúsculas bien puestas.
Ej: Si recibe “lista[x]s dEsordENAdas” debe retornar “lista[x]s,
Desordenadas”
8. Crear una función que reciba una lista de lista[x]s y las devuelva en una sola
cadena en modo de escalera.
"""
# 1.Crear una función que reciba como parámetro una cadena y determine
# cuántas lista[x]s contiene. La función deberá retornar un entero indicando el
# número de lista[x]s.

def ejercicio1(cadena:str):
    
    cadena = cadena.replace(",","")
    lista = cadena.split(" ")
    return len(lista)

# 2. Crear una función que reciba como parámetro una cadena y devuelva la
# misma cadena pero con cada lista[x] empezando con una letra mayúscula.
# Ej: Si recibe como parámetro la cadena "hola mundo" debe devolver "Hola
# Mundo".

def ejercicio2(cadena:str):
    
    cadena = cadena.replace(",","")
    lista = cadena.split()
    
    for i in range(len(lista)):
        
        lista[i] = lista[i].capitalize()
    
    separador = " "
    cadena = separador.join(lista)

    return cadena

""""
3. Crear una función que reciba una cadena y devuelva una nueva cadena donde
todas las lista[x]s de posición impar sean eliminadas.
Ej: Si recibe la cadena "Este es un ejemplo" debe devolver "Este un".
"""
def ejercicio3(cadena:str):
    
    cadena = cadena.replace(",","")
    lista = cadena.split()
    almacenador_pares = " "
    
    for i in range(len(lista)):
        
        if i % 2 == 0:
                            
            almacenador_pares += lista[i] + " "

            almacenador_pares.strip()
    
    return almacenador_pares

# Crear una función que reciba una cadena y devuelva esa misma cadena pero
# con todas las letras en posición par en mayúsculas.
# Ej: Si recibe la cadena “ejemplo”, debe devolver “eJeMpLo”

def ejercicio4(cadena:str):
    
    cadena = cadena.replace(",","")
    lista = cadena.split()
    lista_aux = []
    
    for x in range(len(lista)):
        
        cadena_aux = ""
        
        for i in range(len(lista[x])):
            
            if i % 2 != 0:
                
                cadena_aux += lista[x][i].upper()

            else:
                
                cadena_aux += lista[x][i].lower()
    
        lista_aux.append(cadena_aux)
    
    cadena_formateada = " ".join(lista_aux)
    
    return cadena_formateada

#Crear una función que reciba una cadena y devuelva la lista[x] más larga de
#la misma.

def ejercicio5(cadena:str):
    
    cadena = cadena.replace(",","")
    lista = cadena.split()
    
    for i in range(len(lista)):
        
        if i == 0 or len(mayor) < len(lista[i]):
            
            mayor = lista[i]
    
    return mayor

#Crear una función que pida un número entero, validando que no se ingresen
#otro tipo de caracteres

def ejercicio6(cadena:str):
        
    if cadena.isnumeric():
        
        msg = "Datos validos"
    else:
        msg = "Datos no validos"

    return msg

#Crear una función que reciba una cadena y la devuelva de manera ordenada y
#con las mayúsculas bien puestas.
#Si recibe “lista[x]s dEsordENAdas” debe retornar “lista[x]s,
#Desordenadas”

def ejercicio7(cadena:str):
    
    cadena = cadena.replace(",","")
    lista = cadena.split()
    lista_aux = []
        
    for i in range(len(lista)):
        
        lista_aux.append(lista[i].capitalize())
    
    cadena_formateada = " ".join(lista_aux)
    
    cadena_formateada = cadena_formateada.replace(" ",", ",1)

    return cadena_formateada

# Crear una función que reciba una lista de lista[x]s y las devuelva en una sola
# cadena en modo de escalera.



def ejercicio8(lista):
    
    for i in range(len(lista)):
        
        for j in range(i+1,len(lista)):
            
            if len(lista[j]) < len(lista[i]):
                
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    
    cadena_escalera_nose = ""
    
    for i in range(len(lista)):
        
        cadena_escalera_nose += f"{lista[i]}\n"

    return cadena_escalera_nose