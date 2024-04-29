#Sohrobigarat Giuliano
# La división de higiene está trabajando en un control de stock para productos
# sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de
# contagio, de cada una debe obtener los siguientes datos:
# 1. El tipo (validar "barbijo", "jabón" o "alcohol")
# 2. El precio: (validar entre 100 y 300)
# 3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
# 1000 unidades)
# 4. La marca y el Fabricante.
# Se debe informar lo siguiente:
# A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
# B. Del ítem con más unidades, el fabricante.
# C. Cuántas unidades de jabones hay en total.


# bandera_primer_barbijo = True
# precio_mas_caro_barbijo = 0
# fabricante_del_barbijo_mas_caro_barbijo = ""
# item_con_mas_unidades = 0
# acumulador_jabon = 0

# for i in range(5):
#     elemento = input('Ingrese el tipo de elemento(Baribjo/Jabón/Alcohol): ')
#     elemento = elemento.lower()
    
#     while(elemento != "barbijo" and elemento != "jabon" and elemento != "alcohol"):
#         print("Tipo de elemento inexsitente, intente nuevamente.")
#         elemento = input("Ingrese el tipo de babijo(Baribjo/Jabón/Alcohol): ")
#         elemento = elemento.lower()
    
#     precio = float(input("Ingrese el precio: "))
    
#     while(precio <100 or precio >300):
#         print("El valor tiene que estar entre 100 y 300, intente nuevamente.")
#         precio = float(input("Ingrese el precio: "))
    
#     cantidad_unidades = int(input("Ingrese la cantidad: "))
    
#     while(cantidad_unidades <= 0 or cantidad_unidades > 1000):
        
#         cantidad_unidades = int(input("Reingrese la cantidad: "))
    
#     marca = input("Ingrese la marca: ")
#     fabricante = input("Ingrese el fabricante: ")    
    
#     if(elemento == "barbijo"):
#         if(bandera_primer_barbijo == True or precio > precio_mas_caro_barbijo):
#             precio_mas_caro_barbijo = precio
#             fabricante_del_barbijo_mas_caro = fabricante
#             mayor_cantidad_barbijos = cantidad_unidades
#             bandera_primer_barbijo = False
#     elif elemento == "jabon":
#         acumulador_jabon += cantidad_unidades

#     if(i == 0 or cantidad_unidades > item_con_mas_unidades): #item con más unidades
#         item_con_mas_unidades = cantidad_unidades
#         fabricante_con_mas_unidades = fabricante

                
# print(f"El fabricante del barbijo mas caro es {fabricante_del_barbijo_mas_caro} y hay {mayor_cantidad_barbijos}.\nEl fabricante de articulos con mayor unidades es {fabricante_con_mas_unidades}.\n Hay {acumulador_jabon} Jabónes.") 
