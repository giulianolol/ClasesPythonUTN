lista_enteros = [5, 7, 2]
nombres = ["Ana", "Mario", "Charly", "Esteban", "Pedro", "Luis"]

def ordenar_lista(lista, ascendente: bool):
    
    contador = 0
        
    for i in range(len(lista)):
        
        for x in range(0, len(lista) - i - 1):
            
            if ascendente:
            
                if lista[x] > lista[x + 1]:
                    
                    lista[x] = lista[x + 1]
                    
                    lista[x+1] = lista[x]
                
                    contador +=1
            else:
                
                if lista[x] < lista[x + 1]:
                    
                    lista[x] = lista[x + 1]
                    
                    lista[x+1] = lista[x]
                    
                    contador +=1
                    
    return contador

def ordenar_nombres(lista_nombres, ascendente:bool):
    
    contador = 0
    
    n = len(lista_nombres)
    
    for i in range(n - 1):
        
        for x in range(0, n - i - 1):
            
            if ascendente:
                
                if lista_nombres[x] > lista_nombres[x + 1]:
                    
                    lista_nombres[x] , lista_nombres[x + 1] = lista_nombres[x + 1] , lista_nombres[x]
                    
                    contador += 1
            else:
                
                if lista_nombres[x] < lista_nombres[x + 1]:
                    
                    lista_nombres[x], lista_nombres[x + 1]  = lista_nombres[x + 1], lista_nombres[x]
                    
                    contador += 1
                    
    return contador

cambios_ascendente = ordenar_nombres(nombres, True)

print(f"Lista de nombres ordenada de la A-Z: ", {nombres})
print(f"Cantidad de cambios: ", {cambios_ascendente})
