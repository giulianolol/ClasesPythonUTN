"""
1. Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el
promedio de todos los números.
2. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el
promedio de los números positivos.
3. Escribir una función que calcule y retorne el producto de todos los elementos de la lista
que recibe como parámetro.
4. Escribir una función que reciba como parámetros una lista de enteros y retorne la posición
del valor máximo encontrado.
5. Escribir una función que reciba como parámetros una lista de enteros y muestre la/las
posiciones en donde se encuentra el valor máximo hallado.
6. Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista
de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe
reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente
reemplazo y luego retornar la cantidad total de reemplazos realizados.
"""

from funciones import *

lista_prueba = ["1","2","3"]
lista_nombres_a_reemplazar = ["1","2"]
lista_nombres_reemplazo = ["7","7"]

contador = 0

for i in range(0,len(lista_nombres_a_reemplazar)):
    
    contador += reemplazar_nombres(lista_prueba, lista_nombres_a_reemplazar[i],lista_nombres_reemplazo[i])
    

print(contador)