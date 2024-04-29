"""
//Sohrobigarat Giuliano
Ejercicio 01: Escribe una función que calcule el área de un círculo. La función debe recibir
el radio como parámetro y devolver el área.
Ejercicio 02: Crea una función que verifique si un número dado es par o impar. La función
debe imprimir un mensaje indicando si el número es par o impar.
Ejercicio 03: Define una función que encuentre el máximo de tres números. La función
debe aceptar tres argumentos y devolver el número más grande.
Ejercicio 04: Diseña una función que calcule la potencia de un número. La función debe
recibir la base y el exponente como argumentos y devolver el resultado.
"""
from Funciones import *

valor_ingresado = pedir_valor()

while (valor_ingresado != "z"):
    
    if valor_ingresado == "a":
        
        area = float(input("Ingrese la medida del radio: "))
        print(f"El area del circulo es {calcular_area_circulo(area)}")
        
        valor_ingresado = pedir_valor()
        
    elif valor_ingresado == "b":
        
        numero = float(input("Ingrese un numero para saber si es par o inpar: "))
        par_o_inpar(numero)
        
        valor_ingresado = pedir_valor()
        
    elif valor_ingresado == "c":
        
        numero1 = float(input("Ingrese 3 numero para saber cual es su maximo 1/3: "))
        numero2 = float(input("Ingrese 3 numero para saber cual es su maximo 2/3: "))
        numero3 = float(input("Ingrese 3 numero para saber cual es su maximo 3/3: "))
        
        print(f"El numero maximo de los numero ingresados es {maximo_de_tres_numeros(numero1,numero2,numero3)}")
        
        valor_ingresado = pedir_valor()

    elif valor_ingresado == "d":
        
        base = float(input("Ingrese la base: "))
        expontente = float(input("Ingrese el expontente: "))
        
        print(f"Resultado: {calcular_potencia(base, expontente)}")
        
        valor_ingresado = pedir_valor()
        
    else: 
        print("Opcion on valida")
        valor_ingresado = input('Ingrese una opción valida.\n - a)Calcular area de un circulo.\n - b)Verificar si un numero es par o no.\n - c)Verificar el mayor numero de los tres.\n - d)Calcular la potencia de un numero.\nIngrese la tecla Z para salir.\nIngrese la letra que desea: ')
        valor_ingresado = valor_ingresado.lower()
        
print("Gracias por utilizar, Saludos!")