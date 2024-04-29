#Esta función calcula el area de un cirulo, recibe el radio(float) y retorna el area(float)

def calcular_area_circulo(radio:float):
    
    area = 3.14 * (radio * radio)
    
    return area

#Esta función recibe un numero y calcula si es par o inpar y no retorna nada. Avisa por consola con un mensaje

def par_o_inpar(numero):
    
    if numero % 2 == 0:
        
        print("El número es par.")
        
    else:
        
        print("El número es inpar.")

#Esta funcion recibe 3 numeros como parametro y devuelve el mayor de los tres.
        
def maximo_de_tres_numeros(numero1, numero2, numero3):
    
    if numero1 > numero2 and numero1 > numero3:
        
        return numero1
    
    elif numero2 > numero1 and numero2 > numero3:
        
        return numero2
    
    else: return numero3

#Esta función recibe 2 numeros en el siguiente orden, base, exponente. Luego retorna la potencia de la base elevado por su exponente

def calcular_potencia(base:float, exponente:float):
    
    for i in range(exponente):
        
        if i == 0:
            
            resultado = base * base
            
        else:
            
            resultado = (resultado * base)

    return resultado

#Esta funcion muestra el menú y pide un valor(str), para luego restornarlo. Su función es ahorrar codigo para que el programa sea más performante.

def pedir_valor():
    valor_ingresado = input('Ingrese la funcion con la que desea operar\n - a)Calcular area de un circulo.\n - b)Verificar si un numero es par o no.\n - c)Verificar el mayor numero de los tres.\n - d)Calcular la potencia de un numero.\nIngrese la tecla Z para salir.\nIngrese la letra que desea: ')

    valor_ingresado = valor_ingresado.lower()
    
    return valor_ingresado