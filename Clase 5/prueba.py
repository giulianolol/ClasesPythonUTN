'''
1. Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el
promedio de todos los números
'''
def calcular_promedio(lista:list):
    if(len(lista) > 0):
        acumulador = 0
        for i in range(len(lista)):
            acumulador = acumulador + lista[i]
        promedio = acumulador / len(lista)
        return promedio
    else:
        return "lista vacia"
lista = []
#print(calcular_promedio(lista))

'''
2. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el
promedio de los números positivos
'''
# def calcular_promedio_positivos(lista):
#     acumulador = 0
#     index_positivo = 0
#     for i in range(len(lista)):
#         if(lista[i] > 0):
#             acumulador += lista[i]
#             index_positivo += 1
#     promedio = acumulador / index_positivo
#     return promedio

# print(calcular_promedio_positivos(lista))

def calcular_promedio_reutilizando(lista):
    lista_positivos = []
    for i in range(len(lista)):
        if(lista[i] > 0):
            lista_positivos.append(lista[i])
    return calcular_promedio(lista_positivos)

print(calcular_promedio_reutilizando(lista))

'''
3. Escribir una función que calcule y retorne el producto de todos los elementos de la lista
que recibe como parámetro
'''

def calcular_producto(lista):
    acumulador = 1
    for i in range(len(lista)):
        acumulador *= lista[i]
    return acumulador

print(calcular_producto(lista))

'''
4. Escribir una función que reciba como parámetros una lista de enteros y retorne la posición
del valor máximo encontrado
'''

# def hallar_maximo(lista):
#     for i in range(len(lista)):
#         if(i == 0 or mayor < lista[i]):
#             mayor = lista[i]
#             posicion = i
#     return posicion

# print(hallar_maximo(lista))

'''
5. Escribir una función que reciba como parámetros una lista de enteros y muestre la/las
posiciones en donde se encuentra el valor máximo hallado
'''

# def hallar_maximos(lista):
#     lista_posiciones = []
#     for i in range(len(lista)):
#         if(i == 0 or mayor < lista[i]):
#             mayor = lista[i]
        
#     for i in range(len(lista)):
#         if(lista[i] == mayor):
#             lista_posiciones.append(i)
#     return lista_posiciones

# print(hallar_maximos(lista))

def hallar_maximos(lista):
    lista_posiciones = []
    for i in range(len(lista)):
        if(i == 0 or mayor < lista[i]):
            mayor = lista[i]
            lista_posiciones = []
            lista_posiciones.append(i)
        elif(lista[i] == mayor):
            lista_posiciones.append(i)
    return lista_posiciones

print(hallar_maximos(lista))

'''
6. Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista
de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe
reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente
reemplazo y luego retornar la cantidad total de reemplazos realizados.
'''
lista = ["-10","-7","-12","-10"]
nombre = "-10"
reemplazo = "1"
def reemplazar_nombres(lista, nombre, reemplazo):
    
    contador = 0
    
    for i in range(len(lista)):
        
        if lista[i] == nombre:
            
            lista[i] = reemplazo
            
            contador += 1

    return contador

prueba = reemplazar_nombres(lista, nombre, reemplazo)

print (prueba)
print (lista)