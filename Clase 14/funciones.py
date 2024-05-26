def mostar_profesores_activos(profesor:dict, lista_profesores):
    
    nombre_y_apellido = ""
    
    if profesor["activo"] == True and len(profesor["clases"]) != 0:
            
        nombre_y_apellido = "Nombre: " + profesor["nombre"] + " - Apellido: " + profesor["apellido"]
            
        lista_profesores.append(nombre_y_apellido)
    
def mostrar_profesores_y_materias(lista:list,conteo_materias:dict):
        
    for profesor in lista:
    
        materias = profesor["materias"]
    
        for materia in materias:
        
            if materia in conteo_materias:
            
                conteo_materias[materia] +=1
            
            else:
                conteo_materias[materia] = 1
            
    for materia, conteo in conteo_materias.items():
    
        print(f"{materia}: {conteo} profesores")

def modificar_info_profesor(profesor:dict):
    
    agregar_o_retirar_clase = input("Ingrese 1 para agregar clase, 2 para retirar")
    
    if agregar_o_retirar_clase== "1":
        
        nombre_clase = input("Ingres el nombre de la clase a agregar: ")
        profesor["clases"].append(nombre_clase)

        
    elif agregar_o_retirar_clase == "2":
        
        nombre_clase = input("Ingres el nombre de la clase a retirar: ")
        profesor["clases"].remove(nombre_clase)
    
    return profesor

def pedir_id_para_modificar_clase(lista):
    
    id_profesor = input("Ingrese el id del profesor")

    id_profesor = int(id_profesor)

    for i in range(len(lista)):
    
        if id_profesor == lista[i]["id"]:
        
            profesor_modificado = modificar_info_profesor(lista[i])
    
    return profesor_modificado

def mostrar_info_profesor(lista):
    
    asdas = {"id":1, "nombre":"a"}

    for i in asdas:

        print(asdas[i].value())

    

    # for diccicionario in lista:
        
    #     diccicionario